from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Request, User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id, User.role != "admin").first()


def block_user(db: Session, user_id: int, duration: Optional[int] = None):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    if duration:
        user.blocked_until = datetime.utcnow() + timedelta(days=duration)
    else:
        user.blocked_until = datetime.max

    db.commit()
    db.refresh(user)

    return user


def get_request(db: Session, request_id: int):
    return db.query(Request).filter(Request.id == request_id).first()


def block_request(db: Session, request_id: int, duration: Optional[int] = None):
    request = get_request(db, request_id)
    if not request:
        return None

    if duration:
        request.blocked_until = datetime.utcnow() + timedelta(days=duration)
    else:
        request.blocked_until = datetime.max
    db.commit()
    db.refresh(request)
    return request
