from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RequestCreate(BaseModel):
    title: str
    description: str
    price_suggestion: Optional[int] = None

    class Config:
        from_attributes = True


class RequestUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price_suggestion: Optional[int] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True


class RequestRead(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    price_suggestion: Optional[int] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
