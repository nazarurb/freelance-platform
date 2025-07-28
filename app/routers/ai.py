from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.engine import SessionLocal
from app.database.models import User
from app.schemas.ai_price import PriceRequest
from app.schemas.request import RequestRead
from app.services.ai_features import (generate_price_suggestion,
                                      generate_report,
                                      generate_title_statistics)

router = APIRouter(prefix="/ai", tags=["AI Features"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/reports/")
def download_report(
        date: str = Query(..., description="Date in YYYY-MM-DD for daily or YYYY-MM for monthly"),
        report_type: str = Query(..., description="Type of report: 'daily' or 'monthly'"),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    data = generate_report(db, date, report_type, current_user)
    return Response(content=data, media_type="text/json")


@router.get("/statistics/")
def download_statistics(
        title: str = Query(..., description="Title to filter requests"),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    data = generate_title_statistics(db, title, current_user)
    return Response(content=data, media_type="text/json")


@router.post("/price/", response_model=RequestRead)
def download_budget(
        request_data: PriceRequest,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    data = generate_price_suggestion(db, request_data.title, request_data.description, current_user)
    return Response(content=data, media_type="text/json")
