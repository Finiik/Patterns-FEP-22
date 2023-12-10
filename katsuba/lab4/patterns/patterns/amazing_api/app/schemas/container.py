from pydantic import BaseModel


class Container(BaseModel):

    id: int
    id_check: int
    weight_check: float
    type_check: int

    class Config:
        orm_mode = True
