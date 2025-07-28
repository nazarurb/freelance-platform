from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.crud.request_crud import (create_request, delete_request,
                                   get_all_requests, get_request,
                                   update_request)
from app.database.engine import SessionLocal
from app.database.models import User
from app.schemas.request import RequestCreate, RequestRead, RequestUpdate

router = APIRouter(prefix="/requests", tags=["requests"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=RequestRead)
def create_request_endpoint(
        request_data: RequestCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    new_req = create_request(db, request_data, current_user.id)
    return new_req


@router.get("/{request_id}", response_model=RequestRead)
def read_request_endpoint(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_req = get_request(db, request_id)
    if not db_req:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found."
        )

    if db_req.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to view this request."
        )

    return db_req


@router.put("/{request_id}", response_model=RequestRead)
def update_request_endpoint(
        request_id: int,
        req_data: RequestUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    db_req = get_request(db, request_id)
    if not db_req:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found.")

    if db_req.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to edit this request."
        )

    updated_req = update_request(db, request_id, req_data)
    return updated_req


@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request_endpoint(
        request_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    db_req = get_request(db, request_id)
    if not db_req:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found.")

    if db_req.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to delete this request."
        )

    success = delete_request(db, request_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Request deletion failed."
        )
    return


@router.get("/", response_model=List[RequestRead])
def get_all_requests_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    requests = get_all_requests(db)
    if not requests:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No requests found."
        )
    return requests
