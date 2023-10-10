from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class ConfigShip:
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float


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

    def __init__(self, port, ship_config: ConfigShip, fuel: float = 0.0) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def set_initial_port(self, port):
        self.port = port

    def get_current_containers(self) -> list:
        sorted_containers = sorted(self.containers, key=lambda container: container.id)
        # lambda container: container.id є анонімною функцією, яка приймає контейнер і повертає його ідентифікатор
        # Це слугує ключем для сортування.
        return sorted_containers

    def sail_to(self, port) -> bool:
        distance = self.port.get_distance(port)
        fuel_needed = distance * self.configs.fuel_consumption_per_km
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.port.outgoing_ship(self)  # Корабель виходить з поточного порту
            arrived_port = self.port  # Запам'ятовуємо порт, до якого корабель прибуває
            self.port = port  # Корабель прибуває в новий порт
            port.incoming_ship(self)  # Корабель входить в новий порт
            print(f"The ship with ID {self.id} has arrived at the destination port {port.id}.")
            return arrived_port  # Повертаємо порт, до якого корабель прибув
        else:
            print(f"The ship with ID {self.id} does not have enough fuel to reach the destination port.")
            return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel
        print(f"The ship with ID {self.id} has been refueled with {amount_of_fuel} units of fuel.")

    def load(self, container) -> bool:
        if len(self.containers) < self.configs.max_number_of_all_containers:
            self.containers.append(container)
            print(f"The ship with ID {self.id} has loaded a container.")
            return True
        else:
            print(f"The ship with ID {self.id} cannot load more containers; it has reached its capacity.")
            return False

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            print(f"The ship with ID {self.id} has unloaded a container.")
            return True
        else:
            print(f"The specified container is not on the ship with ID {self.id}.")
            return False


