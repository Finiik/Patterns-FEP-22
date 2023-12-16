"""Holds details about port objects"""

from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import uuid4
from ship import Ship
from container import Container

import haversine as hs


class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass


class Port(IPort):

    def __init__(self, id: uuid4, latitude: float, longitude: float, currentContainersInPort: Container = []) -> None:
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self._currentContainersInPort = currentContainersInPort
        self.shipHistory = []
        self.currentShips = []

    def __str__(self) -> str:
        return (f"ID: {self.id}\nLatitude: {self.latitude}\nLongitude: {self.longitude}\n"
                f"CurrentShips: {self.currentShips}\nCurrentContainers: [{self.currentContainersInPort}]")

    @property
    def current_cont(self):
        return self._currentContainersInPort

    @current_cont.setter
    def current_cont(self, value):
        self.current_cont = value

    def deleteContainer(self, containerID) -> str:
        if not self.current_cont:
            raise AttributeError(f"Container with ID {containerID} has not been found.")
        for container in self.current_cont:
            if type(container) != str:
                if container.id == containerID:
                    self.current_cont.remove(container)
                    return f"Container {containerID} has been successfully removed from port {self.id}"
            elif type(container) == str:
                continue

    def get_distance(self, otherPort: Port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (otherPort.latitude, otherPort.longitude))
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.currentShips:
            self.currentShips.append(ship)
            return True
        else:
            print(f"Failed to add {ship.id} to current ship list.\nCurrent ships are:{self.currentShips}")
            return False

    def outgoing_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship in self.currentShips:
            self.shipHistory.append(ship)
            print(f"Ship {ship.id} was successfully added to port {self.id}.")
            return True
        else:
            print(f"Failed to load ship {ship.id} to port {self.id}.")
            return False
