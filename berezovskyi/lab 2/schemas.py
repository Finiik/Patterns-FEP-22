# schemas.py
from pydantic import BaseModel


class ShipCreate(BaseModel):
    name: str


class ContainerCreate(BaseModel):
    content: str
