from abc import ABC, abstractmethod
from pydantic import BaseModel

from app.schemas.port import Port
from app.schemas.containers import *


class IShip(BaseModel, ABC):
    title: str
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km_litres: float
    available_fuel: float
    current_port: Port
    current_containers: list[Container]
    id: int

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

    class Config:
        orm_mode = True


class LightWeightShip(IShip, ABC):
    type: str = "Light Weight"
    total_weight_capacity: int = 40_000
    fuel_consumption_per_km_litres: int = 20
    available_fuel: int = 10_000
    ship_type_fuel_multiplier: int = 0.5

    def sail_to(self, port: Port) -> bool:
        amount_of_fuel_needed = (self.fuel_consumption_per_km_litres * self.ship_type_fuel_multiplier
                                 * port.get_distance(self.current_port))
        if amount_of_fuel_needed < self.available_fuel:
            self.refuel(self.available_fuel - amount_of_fuel_needed)

        port.incoming_ship(self)
        self.current_port.outgoing_ship(self)
        return True

    def refuel(self, amount_of_fuel_to_add: float) -> None:
        if amount_of_fuel_to_add < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        else:
            self.available_fuel += amount_of_fuel_to_add

    def load(self, container: Container) -> bool:
        pass

    def unload(self, container: Container) -> bool:
        pass


class MediumWeightShip(IShip, ABC):
    type: str = "Medium Weight"
    total_weight_capacity: int = 70_000
    available_fuel: int = 10_000
    ship_type_fuel_multiplier: int = 1.5

    def sail_to(self, port) -> bool:
        amount_of_fuel_needed = (self.fuel_consumption_per_km_litres * self.ship_type_fuel_multiplier
                                 * port.get_distance(self.current_port))
        if amount_of_fuel_needed < self.available_fuel:
            self.refuel(self.available_fuel - amount_of_fuel_needed)

        port.incoming_ship(self)
        self.current_port.outgoing_ship(self)
        return True

    def refuel(self, amount_of_fuel_to_add: float) -> None:
        if amount_of_fuel_to_add < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        else:
            self.available_fuel += amount_of_fuel_to_add
            print(f"{amount_of_fuel_to_add} liters has been added to available fuel."
                  f"Current fuel available: {self.available_fuel}")

    def load(self, container) -> bool:
        pass

    def unload(self, container) -> bool:
        pass


class HeavyWeightShip(IShip, ABC):
    type: str = "Heavy Weight"
    total_weight_capacity: int = 100_000
    available_fuel: int = 10_000
    ship_type_fuel_multiplier: int = 2.5

    def sail_to(self, port) -> bool:
        amount_of_fuel_needed = (self.fuel_consumption_per_km_litres * self.ship_type_fuel_multiplier
                                 * port.get_distance(self.current_port))
        if amount_of_fuel_needed < self.available_fuel:
            self.refuel(self.available_fuel - amount_of_fuel_needed)

        port.incoming_ship(self)
        self.current_port.outgoing_ship(self)
        return True

    def refuel(self, amount_of_fuel_to_add: float) -> None:
        if amount_of_fuel_to_add < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        else:
            self.available_fuel += amount_of_fuel_to_add
            print(f"{amount_of_fuel_to_add} liters has been added to available fuel."
                  f"Current fuel available: {self.available_fuel}")

    def load(self, container) -> bool:
        pass

    def unload(self, container) -> bool:
        pass
