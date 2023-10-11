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

    @abstractmethod
    def get_distance(self, port) -> float:
        pass

    @abstractmethod
    def refuel_ship(self, ship: Ship, amount_of_fuel: float) -> None:
        pass


class Port(IPort):
    """Implements port logic"""

    def __init__(self, latitude: float, longitude: float) -> None:
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True

    def outgoing_ship(self, ship: Ship) -> bool:
        if ship in self.current_ships:
            self.ship_history.append(ship)
            self.current_ships.remove(ship)
            return True
        else:
            print(f"The ship with ID {ship.id} is not in the current ships list of the port.")
            return False

    def refuel_ship(self, ship: Ship, amount_of_fuel: float) -> None:
        ship.refuel(amount_of_fuel)
