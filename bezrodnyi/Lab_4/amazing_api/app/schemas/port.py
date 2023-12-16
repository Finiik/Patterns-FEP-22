from abc import ABC, abstractmethod
from typing import List
import haversine as hs
from pydantic import BaseModel

from app.schemas.items import *
from app.schemas.containers import *


class IPort(BaseModel, ABC):
    """Basic abstraction"""

    id: int

    @abstractmethod
    def incoming_ship(self, ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship):
        pass

    class Config:
        from_attributes = True


class Port(IPort):
    """Implements port logic"""
    latitude: float
    longitude: float
    title: str
    items: List[Item] = []
    containers: List[Container] = []
    current_ships: List[int] = []
    ship_history: List[int] = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship_id) -> None:
        if ship_id not in self.current_ships:
            self.current_ships.append(ship_id)

    def outgoing_ship(self, ship_id) -> None:
        if ship_id in self.current_ships:
            self.current_ships.remove(ship_id)
            self.ship_history.append(ship_id)
