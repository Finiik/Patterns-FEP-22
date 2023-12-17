from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from dataclasses import dataclass
from containers import Container

if TYPE_CHECKING:
    from port import Port


@dataclass
class ConfigShip:

    def __init__(self, total_weight_capacity, max_number_of_all_containers, maxNumberOfHeavyContainers,
                 maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers, maxNumberOfBasicContainers,
                 fuelConsumptionPerKM):
        self.total_weight_capacity = total_weight_capacity
        self.max_number_of_all_containers = max_number_of_all_containers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.maxNumberOfBasicContainers = maxNumberOfBasicContainers
        self.fuelConsumptionPerKM = fuelConsumptionPerKM


class IShip(ABC):

    @abstractmethod
    def sail_to(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass


class Ship(IShip):
    """Ship implementation"""

    def __init__(self, ship_id, port, port_deliver, ship_config: ConfigShip, fuel: float = 0.0) -> None:
        self.id = ship_id
        self.fuel = fuel
        self.port = port
        self.port_deliver = port_deliver
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        # TODO: refactor
        self.containers = sorted(self.containers, key=lambda container: container.id)
        return self.containers

    def sail_to(self, port: Port) -> bool:
        # if isinstance(port, Port):
        distance = self.fuel / self.configs.fuelConsumptionPerKM
        if distance >= self.port.get_distance(port):
            port.incoming_ship(self)
            self.port.outgoing_ship(self)
            print(f"ship {self} sail to port {port}")
            return True
        else:
            print(f"ship {self} hasnt enough fuel to sail to port {port}")
            return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel = self.fuel + amount_of_fuel
        print(f"ship {self} refueld ok")

    def load(self, container: Container) -> bool:
        self.containers.append(container)
        print(f"container {container} load into ship {self}")
        return True

    def unload(self, container: Container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            print(f"container {container} unload from ship {self}")
            return True
        else:
            print(f"container {container} not in ship {self}")
            return False



class LightWeightShip(Ship):
    def __repr__(self):
        return f"The ship {self.id} is a lightweight ship."
    pass


class MediumShip(Ship):
    def __repr__(self):
        return f"The ship {self.id}is a medium ship."
    pass


class HeavyShip(Ship):
    def __repr__(self):
        return f"The ship {self.id} is a heavy ship."
    pass


class ShipFactory:

    def create_ship(self, ship_type, ship_id, port, port_deliver, ship_config: ConfigShip, fuel: float = 0.0):
        if ship_type == 'LightWeightShip':
            return LightWeightShip(ship_id, port, port_deliver, ship_config, fuel)
        elif ship_type == 'MediumShip':
            return MediumShip(ship_id, port, port_deliver, ship_config, fuel)
        elif ship_type == 'HeavyShip':
            return HeavyShip(ship_id, port, port_deliver, ship_config, fuel)
        else:
            raise ValueError(f"Invalid item type: {ship_type}")
