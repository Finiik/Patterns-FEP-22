from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import uuid4
from ship import ShipСlass
from containers import *

import haversine as hs


class IPort(ABC):

    @abstractmethod
    def incomingShip(self, ship: ShipСlass):
        pass

    @abstractmethod
    def outgoingShip(self, ship: ShipСlass):
        pass


class PortClass(IPort):
    """Implements port logic"""

    def __init__(self, id: uuid4, latitude: float, longitude: float, currentContainersInPort: Container = []) -> None:
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self._currentContainersInPort = currentContainersInPort
        self.shipHistory = []
        self.currentShips = []

    def __str__(self) -> str:
        return f"ID: {self.id}\nLatitude: {self.latitude}\nLongitude: {self.longitude}\nCurrentShips: {self.currentShips}\nCurrentContainers: [{self.currentContainersInPort}]"

    @property
    def currentContainersInPort(self):
        return self._currentContainersInPort

    @currentContainersInPort.setter
    def currentContainersInPort(self, value):
        self.currentContainersInPort = value

    def deleteContainer(self, containerID) -> str:
        if not self.currentContainersInPort:
            raise AttributeError(f"Container with ID {containerID} has not been found.")
        for container in self.currentContainersInPort:
            if type(container) != str:
                if container.id == containerID:
                    self.currentContainersInPort.remove(container)
                    return f"Container {containerID} has been successfully removed from port {self.id}"
            elif type(container) == str:
                continue

    def getDistance(self, otherPort: PortClass) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (otherPort.latitude, otherPort.longitude))
        return dist

    def incomingShip(self, ship: ShipСlass) -> bool:
        if isinstance(ship, ShipСlass) and ship not in self.currentShips:
            self.currentShips.append(ship)
            return True
        else:
            print(f"Failed to add {ship.id} to current ship list.\nCurrent ships are:{self.currentShips}")
            return False

    def outgoingShip(self, ship: ShipСlass) -> bool:
        if isinstance(ship, ShipСlass) and ship in self.currentShips:
            self.shipHistory.append(ship)
            print(f"Ship {ship.id} was successfully added to port {self.id}.")
            return True
        else:
            print(f"Failed to load ship {ship.id} to port {self.id}.")
            return False
