from pydantic import BaseModel


class Item(BaseModel):
    id: int
    weight: int
    count: int
    container_id: int

    class Config:
        orm_mode = True
