from pydantic import BaseModel


class DeliveryItem(BaseModel):
    id: str
    name: str
    quantity: int
