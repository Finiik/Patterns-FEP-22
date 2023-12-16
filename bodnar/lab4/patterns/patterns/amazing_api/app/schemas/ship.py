from pydantic import BaseModel


class Ship(BaseModel):
    id: int
    fuel: float
    ship_id: int
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float

    class Config:
        orm_mode = True


class CreateShip(Ship):
    pass

    class Config:
        orm_mode = True
