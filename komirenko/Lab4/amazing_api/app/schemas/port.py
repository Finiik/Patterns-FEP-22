from abc import ABC, abstractmethod
from typing import List
#import haversine as hs
from pydantic import BaseModel

from app.schemas.ship import IShip
# from app.schemas.items import Item
# from app.schemas.containers import Container


class IPort(BaseModel, ABC):
    """Basic abstraction"""

    id: int

    @abstractmethod
    def incoming_ship(self, ship: IShip):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: IShip):
        pass

    class Config:
        orm_mode = True


class Port(IPort):
    """Implements port logic"""

    title: str
    basic: int
    heavy: int
    refrigerated: int
    liquid: int
    latitude: float
    longitude: float
    # items: List[Item] = []
    # containers: List[Container] = []
    ship_history: List[int] = []
    current_ships: List[int] = []

    def get_distance(self, port) -> float:
        dist = 1000
        #dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship: IShip) -> None:
        if isinstance(ship, IShip) and ship not in self.current_ships:
            self.current_ships.append(ship.id)

    def outgoing_ship(self, ship: IShip) -> None:
        if isinstance(ship, IShip) and ship.id in self.current_ships:
            self.ship_history.append(ship.id)

