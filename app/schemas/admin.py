from datetime import datetime

from pydantic import BaseModel


class AdminActionCreate(BaseModel):
    action: str

    class Config:
        from_attributes = True


class AdminActionRead(BaseModel):
    id: int
    admin_id: int
    action: str
    timestamp: datetime

    class Config:
        from_attributes = True
