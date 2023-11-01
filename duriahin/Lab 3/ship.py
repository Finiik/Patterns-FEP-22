from __future__ import annotations
from uuid import UUID, uuid4
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from containers import Container
    from port import Port


@dataclass
class ConfigShip:
    """Dataclass containing Configuration of a Ship"""
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float


class IShip(ABC):
    """Interface of a Ship with abstract methods."""

    @abstractmethod
    def sail_to(self, port: Port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container_id: UUID) -> None:
        pass

    @abstractmethod
    def unload(self, container_id: UUID) -> None:
        pass


class Ship(IShip):
    """Ship implementation"""

    def __init__(self, ship_id: int, port: List[Port], ship_config: ConfigShip, containers: List[Container], fuel: float = 0.0) -> None:
        self.id = ship_id
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self._containers_on_ship = containers
        self._containers_on_ship_id = [container.id if not isinstance(container, str) else container for container in containers]
        self._used_ports_id = []
        self._used_containers = []
        self._unloaded_containers_id = []

    def __str__(self) -> str:
        return (f"id: {self.id}\nfuel: {self.fuel}\nport: {self.port}\n"
                f"configs:\n\t{self.configs}\ncontainers: {self._containers_on_ship}")

    @property
    def containers_on_ship(self) -> List[Container]:
        return self._containers_on_ship

    @property
    def containers_on_ship_id(self) -> List[UUID]:
        ship_containers_id = []
        for ship_container in self._containers_on_ship:
            if type(ship_container) == str:
                ship_containers_id.append(ship_container)
                continue
            else:
                ship_containers_id.append(ship_container.id)
        self._containers_on_ship_id = ship_containers_id
        return self._containers_on_ship_id

    @property
    def used_ports_id(self) -> List[UUID]:
        return self._used_ports_id

    def get_extra_fuel_consumption_from_container(self) -> float:
        extra_fuel = 0
        for ship_container in self._containers_on_ship:
            if type(ship_container) != str:
                extra_fuel += ship_container.consumption()
            elif type(ship_container) == str:
                continue
        return extra_fuel

    def sail_to(self, port: Port) -> bool:
        for current_port in self.port:
            distance = int(port.get_distance(current_port))
            fuel_required = distance / self.configs.fuel_consumption_per_km + self.get_extra_fuel_consumption_from_container()

            if fuel_required < self.fuel and current_port.id not in self._used_ports_id:
                current_port.incoming_ship(self)
                self._used_ports_id.append(current_port.id)
                print(f"Ship {self.id} was sent to {port.id} successfully.")
                return True
            elif current_port.id in self._used_ports_id:
                continue
            else:
                self.refuel(fuel_required - self.fuel)
                current_port.incoming_ship(self)
                self._used_ports_id.append(current_port.id)
                print(f"Ship {self.id} now has {self.fuel} and has been successfully sent to port {port.id}")
                return True

        print(f"Ship {self.id} couldn't find a suitable port.")
        return False

    def refuel(self, amount_of_fuel_to_add: float) -> None:
        if amount_of_fuel_to_add < 0:
            raise ValueError("Amount of fuel given is less than 0.")
        print(f"{amount_of_fuel_to_add} liters has been added to previous amount of fuel: {self.fuel}.")
        self.fuel += amount_of_fuel_to_add

    def check_compatibility_of_ship_and_container(self, i: int) -> bool:
        if self._containers_on_ship[i].weight <= self.configs.total_weight_capacity:
            return True
        else:
            return False

    def delete_container_on_ship(self, container_id: uuid4) -> None:
        containers = [container for container in self._containers_on_ship if container.id != container_id]
        self._containers_on_ship = containers

    def load(self, container_id: UUID) -> None:
        print("Loading container...")
        current_containers_on_ship = self.containers_on_ship
        for i in range(len(current_containers_on_ship)):
            for current_port in self.port:
                if isinstance(current_containers_on_ship[i], str):
                    break
                elif container_id == current_containers_on_ship[i].id and self.check_compatibility_of_ship_and_container(i):
                    container = current_containers_on_ship[i]
                    current_containers_on_ship.append(container)
                    current_port.delete_container(container.id)
                    print(f"Container {container.id} has been successfully loaded.")
                    self._used_containers.append(container.id)
                    if i > 0 and len(self._used_containers) >= 2 and container.id == self._used_containers[-2]:
                        break

    def unload(self, container_id: UUID) -> None:
        container_found = False
        for i, ship_container in enumerate(self._containers_on_ship):
            for current_port in self.port:
                if type(ship_container) == str:
                    break
                elif container_id == ship_container.id and container_id not in self._unloaded_containers_id:
                    self._containers_on_ship.pop(i)
                    current_port.current_containers_in_port.append(ship_container)
                    self._unloaded_containers_id.append(container_id)
                    print(f"Container {container_id} has been successfully unloaded.")
                    container_found = True
                    break

        if not container_found:
            print(f"Container with ID {container_id} not found.")

    @containers_on_ship.setter
    def containers_on_ship(self, value: List[Container]):
        self._containers_on_ship = value


class LightWeightShip(Ship):
    def __repr__(self):
        return f"The ship {self.id} is a lightweight ship."


class MediumShip(Ship):
    def __repr__(self):
        return f"The ship {self.id} is a medium ship."


class HeavyShip(Ship):
    def __repr__(self):
        return f"The ship {self.id} is a heavy ship."


class ShipBuilder:
    def __init__(self, ship_type: str, port: 'Port', ship_id: UUID, fuel: float):
        self.ship_type = ship_type
        self.port = port
        self.ship_id = ship_id
        self.fuel = fuel
        self.configs = None
        self.containers = []

    def set_configs(self, total_weight_capacity, max_num_all, max_num_heavy,
                    max_num_refrigerated, max_num_liquid,
                    fuel_consumption_per_km):
        self.configs = ConfigShip(
            total_weight_capacity=total_weight_capacity,
            max_number_of_all_containers=max_num_all,
            max_number_of_heavy_containers=max_num_heavy,
            max_number_of_refrigerated_containers=max_num_refrigerated,
            max_number_of_liquid_containers=max_num_liquid,
            fuel_consumption_per_km=fuel_consumption_per_km
        )
        return self

    def add_container(self, container: Container):
        self.containers.append(container)
        return self

    def build(self):
        if self.ship_type == 'LightWeightShip':
            return LightWeightShip(
                id=self.ship_id,
                fuel=self.fuel,
                port=self.port,
                ship_config=self.configs,
                containers=self.containers
            )
        elif self.ship_type == 'MediumShip':
            return MediumShip(
                id=self.ship_id,
                fuel=self.fuel,
                port=self.port,
                ship_config=self.configs,
                containers=self.containers
            )
        elif self.ship_type == 'HeavyShip':
            return HeavyShip(
                id=self.ship_id,
                fuel=self.fuel,
                port=self.port,
                ship_config=self.configs,
                containers=self.containers
                )
        else:
            raise ValueError("Invalid ship type")
