from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import UUID
from ship import Ship
from containers import Container
from typing import List
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer


import haversine as hs


class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship) -> bool:
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship) -> bool:
        pass


class Port(IPort):

    def _clear_excess_containers(self):
        allowed_container_types = {'BasicContainer', 'HeavyContainer', 'RefrigeratedContainer', 'LiquidContainer'}
        self._current_containers_in_port = [container for container in self._current_containers_in_port
                                            if isinstance(container, (
            BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer))]

    def __init__(self, port_id: str, latitude: float, longitude: float,
                 current_containers_in_port: List[Container] = ()) -> None:
        self.id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self._current_containers_in_port = current_containers_in_port
        self.ship_history = []
        self.current_ships = []
        self._clear_excess_containers()

    def __str__(self) -> str:
        return (f"ID: {self.id}\nLatitude: {self.latitude}\nLongitude: {self.longitude}\n"
                f"CurrentShips: {self.current_ships}\nCurrentContainers: {self._current_containers_in_port}")

    @property
    def current_containers(self) -> List[Container]:
        return self._current_containers_in_port

    def delete_container(self, container_id: UUID) -> str:
        if not self.current_containers:
            raise ValueError(f"Container with ID {container_id} has not been found.")
        item_to_remove = next((item for item in self.current_containers if item.id == container_id), None)
        if item_to_remove is not None:
            self.current_containers.remove(item_to_remove)
            return f"Container {container_id} has been successfully removed from port {self.id}"
        else:
            return f"Container with ID {container_id} not found in Port {self.id}."
        
    def get_distance(self, other_port: Port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (other_port.latitude, other_port.longitude))
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True
        else:
            raise ValueError(f"Failed to add {ship.id} to current ship list. Current ships are: {self.current_ships}")

    def outgoing_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship in self.current_ships:
            self.ship_history.append(ship)
            print(f"Ship {ship.id} was successfully added to port {self.id}.")
            return True
        else:
            raise ValueError(f"Failed to load ship {ship.id} to port {self.id}.")

    @property
    def current_containers_in_port(self) -> List[Container]:
        return self._current_containers_in_port
