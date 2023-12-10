from typing import List

from pydantic import BaseModel

from app.schemas.ship import Ship


class Port(BaseModel):

    id: int
    title: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class CreatePort(Port):
    pass


class ReadPort(Port):
    ship_history: List[Ship] = []
    current_ships: List[Ship] = []

    class Config:
        orm_mode = True
