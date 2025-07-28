from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.crud.admin_crud import (block_request, block_user, get_request,
                                 get_user)
from app.database.engine import SessionLocal
from app.database.models import Request, User
from app.schemas.request import RequestRead, RequestUpdate
from app.schemas.user import UserRead, UserUpdate
from app.utils.logger import admin_logger, error_logger
from app.utils.security import admin_required

router = APIRouter(prefix="/admin", tags=["admin"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users/{user_id}", response_model=UserRead)
@admin_required
def read_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    user = get_user(db, user_id)
    if not user or user.role == "admin":
        error_logger.warning(f"Unauthorized access attempt to user {user_id} by {current_user.id}")
        raise HTTPException(status_code=404, detail="User not found or is an admin")
    admin_logger.info(f"Admin {current_user.id} accessed user {user_id}")
    return user


@router.put("/users/{user_id}", response_model=UserRead)
@admin_required
def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        error_logger.warning(f"Update failed: User {user_id} not found by {current_user.id}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if user.role == "admin":
        error_logger.warning(f"Attempt to update another admin {user_id} by {current_user.id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot update another admin"
        )

    user.username = user_data.username or user.username
    user.email = user_data.email or user.email

    db.commit()
    db.refresh(user)
    admin_logger.info(f"Admin {current_user.id} updated user {user_id}")
    return user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@admin_required
def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            error_logger.warning(f"❌ Delete failed: User {user_id} not found by {current_user.id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        if user.role == "admin":
            error_logger.warning(
                f"❌ Attempt to delete another admin {user_id} by {current_user.id}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot delete another admin"
            )

        db.delete(user)
        db.commit()

        admin_logger.info(f"✅ Admin {current_user.id} deleted user {user_id}")
        return

    except Exception as e:
        error_logger.error(f"🔥 ERROR in delete_user_endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/users/block/{user_id}", response_model=UserRead)
@admin_required
def block_user_endpoint(
    user_id: int,
    duration: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        error_logger.warning(f"Block failed: User {user_id} not found by {current_user.id}")
        raise HTTPException(status_code=404, detail="User not found")

    if user.role == "admin":
        error_logger.warning(f"Attempt to block another admin {user_id} by {current_user.id}")
        raise HTTPException(status_code=403, detail="Cannot block another admin")

    if duration is not None and duration <= 0:
        raise HTTPException(status_code=400, detail="Invalid duration")

    updated_user = block_user(db, user_id, duration)
    admin_logger.info(f"Admin {current_user.id} blocked user {user_id} for {duration} days")
    return updated_user


@router.put("/users/unblock/{user_id}", response_model=UserRead)
@admin_required
def unblock_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.role == "admin":
        raise HTTPException(status_code=403, detail="Cannot unblock another admin")

    user.blocked_until = None

    db.commit()
    db.refresh(user)
    admin_logger.info(f"Admin {current_user.id} unblocked user {user_id}")

    return user


@router.get("/requests/{request_id}", response_model=RequestRead)
@admin_required
def read_request_endpoint(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    request = get_request(db, request_id)

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    admin_logger.info(f"Admin {current_user.id} read request {request_id}")

    return request


@router.put("/requests/{request_id}", response_model=RequestRead)
@admin_required
def update_request_endpoint(
    request_id: int,
    request_data: RequestUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    request = db.query(Request).filter(Request.id == request_id).first()

    if not request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

    request.title = request_data.title or request.title
    request.description = request_data.description or request.description
    request.price_suggestion = request_data.price_suggestion or request.price_suggestion
    request.status = request_data.status or request.status

    db.commit()
    db.refresh(request)
    admin_logger.info(f"Admin {current_user.id} updated request {request_id}")

    return request


@router.delete("/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
@admin_required
def delete_request_endpoint(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    request = db.query(Request).filter(Request.id == request_id).first()

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    if request.user_id is None:
        raise HTTPException(status_code=400, detail="Request must be associated with a user")

    db.delete(request)
    db.commit()
    admin_logger.info(f"Admin {current_user.id} deleted request {request_id}")

    return


@router.put("/requests/block/{request_id}", response_model=RequestRead)
@admin_required
def block_request_endpoint(
    request_id: int,
    duration: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    request = db.query(Request).filter(Request.id == request_id).first()

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    if request.user_id is None:
        raise HTTPException(status_code=400, detail="Request must be associated with a user")

    if duration is not None and duration <= 0:
        raise HTTPException(status_code=400, detail="Invalid duration")

    blocked_request = block_request(db, request_id, duration)
    admin_logger.info(f"Admin {current_user.id} blocked request {request_id}")

    return blocked_request


@router.put("/requests/unblock/{request_id}", response_model=RequestRead)
@admin_required
def unblock_request_endpoint(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    request = db.query(Request).filter(Request.id == request_id).first()

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    if request.user_id is None:
        raise HTTPException(status_code=400, detail="Request must be associated with a user")

    request.blocked_until = None

    db.commit()
    db.refresh(request)
    admin_logger.info(f"Admin {current_user.id} unblocked request {request_id}")

    return request
