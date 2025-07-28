from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None

    class Config:
        from_attributes = True


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    blocked_until: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True
