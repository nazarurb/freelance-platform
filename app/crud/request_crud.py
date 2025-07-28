from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Request
from app.schemas.request import RequestCreate, RequestUpdate


def get_request(db: Session, request_id: int) -> Optional[Request]:
    return db.query(Request).filter(Request.id == request_id).first()


def create_request(db: Session, request_data: RequestCreate, user_id: int) -> Request:
    db_request = Request(
        user_id=user_id,
        title=request_data.title,
        description=request_data.description,
        price_suggestion=request_data.price_suggestion,
        created_at=datetime.utcnow()
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def update_request(db: Session, request_id: int, update_data: RequestUpdate) -> Optional[Request]:
    db_request = get_request(db, request_id)
    if not db_request:
        return None

    if update_data.title is not None:
        db_request.title = update_data.title
    if update_data.description is not None:
        db_request.description = update_data.description
    if update_data.price_suggestion is not None:
        db_request.price_suggestion = update_data.price_suggestion
    if update_data.status is not None:
        db_request.status = update_data.status

    db.commit()
    db.refresh(db_request)
    return db_request


def delete_request(db: Session, request_id: int) -> bool:
    db_request = get_request(db, request_id)
    if not db_request:
        return False
    db.delete(db_request)
    db.commit()
    return True


def get_all_requests(db: Session):
    return db.query(Request).all()
