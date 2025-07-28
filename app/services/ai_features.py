import csv
import io
import json
from datetime import datetime

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.core.dependencies import get_current_user
from app.database.models import Request, User
from app.services.ai_model import AIModel
from app.services.ai_prompts import (generate_budget_prompt_from_template,
                                     generate_report_prompt_from_template,
                                     generate_statistics_prompt_from_template)

ai_model = AIModel()


def generate_report(
        db: Session,
        date: str,
        report_type: str,
        current_user: User = Depends(get_current_user)
):
    try:
        if report_type == "daily":
            query_date = datetime.strptime(date, "%Y-%m-%d").date()
            requests = db.query(Request).filter(
                extract("year", Request.created_at) == query_date.year,
                extract("month", Request.created_at) == query_date.month,
                extract("day", Request.created_at) == query_date.day
            ).all()
        elif report_type == "monthly":
            query_date = datetime.strptime(date, "%Y-%m").date()
            requests = db.query(Request).filter(
                extract("year", Request.created_at) == query_date.year,
                extract("month", Request.created_at) == query_date.month
            ).all()
        else:
            raise HTTPException(
                status_code=400,
                detail="Invalid report type. Choose 'daily' or 'monthly'."
            )

        if not requests:
            raise HTTPException(status_code=404, detail="No requests found for the given date.")

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Title", "Budget", "Description"])
        for request in requests:
            writer.writerow([request.title, request.price_suggestion, request.description])

        prompt = generate_report_prompt_from_template(str(output.getvalue().encode()))
        ai_summary = ai_model.generate_text(prompt, max_tokens=2048)

        response = {
            "report": ai_summary,
        }
        return json.dumps(response)

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Use YYYY-MM for monthly or YYYY-MM-DD for daily."
        )


def generate_title_statistics(
        db: Session,
        title: str,
        current_user: User = Depends(get_current_user)
):
    requests = (
        db.query(Request)
        .filter(Request.title == title)
        .order_by(Request.created_at.desc())
        .limit(5)
        .all()
    )

    if not requests:
        raise HTTPException(status_code=404, detail="No matching requests found.")

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Title", "Budget", "Description"])
    for request in requests:
        writer.writerow([request.title, request.price_suggestion, request.description])

    prompt = generate_statistics_prompt_from_template(str(output.getvalue().encode()))
    ai_stats = ai_model.generate_text(prompt, max_tokens=2048)

    response = {
        "statistics": ai_stats,
    }
    return json.dumps(response)


def generate_price_suggestion(
        db: Session,
        title: str,
        description: str,
        current_user: User = Depends(get_current_user)
):
    requests = (
        db.query(Request)
        .filter(Request.title == title)
        .order_by(Request.created_at.desc())
        .limit(20)
        .all()
    )

    if not requests:
        raise HTTPException(status_code=404, detail="No matching requests found.")

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Title", "Budget"])
    for request in requests:
        writer.writerow([request.title, request.price_suggestion])

    new_request = {
        "title": title,
        "description": description
    }

    prompt = generate_budget_prompt_from_template(
        new_request=str(new_request),
        input=str(output.getvalue().encode())
    )
    ai_budget = ai_model.generate_text(prompt, max_tokens=2048)

    return ai_budget
