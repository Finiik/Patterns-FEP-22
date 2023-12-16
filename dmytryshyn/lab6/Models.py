from pydantic import BaseModel


class CustomerModel(BaseModel):
    item: str
    amount: int
    card_number: str
    shipment_type: str