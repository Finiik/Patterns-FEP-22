"""Holds details about port objects"""

from abc import ABC, abstractmethod
from uuid import uuid4
from ship import Ship

import haversine as hs


class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass


class Port(IPort):
    """Implements port logic"""

    def __init__(self, port_id, latitude: float, longitude: float) -> None:
        self.id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.basic = []
        self.heavy = []
        self.liquid = []
        self.refrigerated = []
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        print(f"dist = {dist}")
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True
        else:
            return False

    def outgoing_ship(self, ship: Ship) -> bool:
        # TODO: add checker
        if isinstance(ship, Ship) and ship in self.current_ships:
            self.current_ships.remove(ship)
            self.ship_history.append(ship)
            return True
        else:
            return False
