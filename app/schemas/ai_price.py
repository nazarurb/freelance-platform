from pydantic import BaseModel


class PriceRequest(BaseModel):
    title: str
    description: str
