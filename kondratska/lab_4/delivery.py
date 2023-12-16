from pydantic import BaseModel
from typing import Optional


class CreatePort(BaseModel):
    latitude: float
    longitude: float


class CreateShip(BaseModel):
    fuel: int
    total_weight_capacity: int
    maxNumberOfAllContainers: int
    maxNumberOfBasicContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: int

    def determine_ship_type(self) -> str:
        if self.total_weight_capacity <= 20000:
            return "LightWeight"
        elif self.total_weight_capacity <= 40000:
            return "Medium"
        elif self.total_weight_capacity <= 60000:
            return "Heavy"
        else:
            return "Unknown"


class CreateContainer(BaseModel):
    weight: int
    type: Optional[str]


class CreateItem(BaseModel):
    weight: int
    count: int
    type: Optional[str]


class DeliveryInput(BaseModel):
    starting_port_id: str
    transitional_port_id: str
    ending_port_id: str
    ship_to_sail_id: str
