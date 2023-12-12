from pydantic import BaseModel


class Item(BaseModel):
    id: str
    weight: int
    count: int
    item_type: str
