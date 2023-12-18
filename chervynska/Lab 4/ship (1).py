from dataclasses import dataclass
from pydantic import BaseModel
from port import Port
from abc import ABC, abstractmethod
from typing import List, Optional
from container import Container


@dataclass
class ShipConfig:
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: int


class IShip(ABC):
    @abstractmethod
    def sail_to(self, p1, p2, p3):
        pass

    @abstractmethod
    def re_fuel(self, new_fuel: float):
        pass

    @abstractmethod
    def load(self, cont):
        pass

    @abstractmethod
    def unload(self, cont):
        pass


class Ship(IShip, BaseModel, ABC):
    id: str
    fuel: float
    current_port: 'Port'
    ships_data: ShipConfig
    ship_type: str
    containers: Optional[List[Container]] = None
    total_weight: int = 0
    total_containers_types: Optional[List] = None
    total_containers_consumption: int = 0
    items: Optional[List] = None

    # ... (rest of the code remains the same)
