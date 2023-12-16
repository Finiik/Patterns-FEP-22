from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from ship import Ship
from container import Container

import haversine as hs
import logging


class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship) -> bool:
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship) -> bool:
        pass


class Port(IPort, ABC):
    def __init__(self, port_id: UUID, latitude: float, longitude: float,
                 basic_containers: List[Container], heavy_containers: List[Container],
                 refrigerated_containers: List[Container], liquid_containers: List[Container]) -> None:
        self.id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.basic_containers = basic_containers
        self.heavy_containers = heavy_containers
        self.refrigerated_containers = refrigerated_containers
        self.liquid_containers = liquid_containers
        self.ship_history = []
        self.current_ships = []
        self._current_containers_in_port = []

    def __str__(self) -> str:
        return (f"ID: {self.id}\nLatitude: {self.latitude}\nLongitude: {self.longitude}\n"
                f"CurrentShips: {self.current_ships}\nCurrentContainers: {self.current_containers_in_port}")

    def delete_container(self, container_id: UUID) -> str:
        """Delete a container by ID from the port."""
        if not self.current_containers_in_port:
            raise AttributeError(f"Container with ID {container_id} has not been found.")
        for container in self.current_containers_in_port:
            if isinstance(container, Container) and container.id == container_id:
                self.current_containers_in_port.remove(container)
                return f"Container {container_id} has been successfully removed from port {self.id}"
        return f"Container with ID {container_id} not found in port {self.id}"

    def get_distance(self, other_port: Port) -> float:
        """Calculate the haversine distance between two ports."""
        coordinates_self = (self.latitude, self.longitude)
        coordinates_other = (other_port.latitude, other_port.longitude)
        dist = hs.haversine(coordinates_self, coordinates_other)
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        """Add a ship to the list of current ships."""
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True
        else:
            logging.error(f"Failed to add {ship.id} to current ship list.\nCurrent ships are:{self.current_ships}")
            return False

    def outgoing_ship(self, ship: Ship) -> bool:
        """Move a ship from the list of current ships to ship history."""
        if isinstance(ship, Ship) and ship in self.current_ships:
            self.ship_history.append(ship)
            logging.info(f"Ship {ship.id} was successfully added to port {self.id}.")
            return True
        else:
            logging.error(f"Failed to load ship {ship.id} to port {self.id}.")
            return False

    @property
    def current_containers_in_port(self) -> List[Container]:
        """Get the list of current containers in the port."""
        return self._current_containers_in_port
