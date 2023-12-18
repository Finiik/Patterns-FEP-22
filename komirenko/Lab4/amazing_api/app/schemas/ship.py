
from abc import ABC, abstractmethod
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories.containers import ContainerRepository




from app.schemas.containers import Container
from typing import List
#from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

class IShip(BaseModel):
    id: int
    title:str
    type_:str
    fuel:int
    port_id: int
    port_deliver: int
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float

    def sail_to(self,db: Session) -> bool:
        distance = self.fuel / self.fuel_consumption_per_km
        if distance >= 1000:
            from app.db.repositories.ships import ShipRepository
            ship_crud = ShipRepository(db)
            self.port_id = self.port_deliver
            self.port_deliver = 0
            ship_crud.update_ship(self)
            print(f"ship {self} sail to port {self.port_deliver}")
            return True

        else:
            print(f"ship {self} hasnt enough fuel to sail to port {self.port_deliver}")
            return False

    def refuel(self, db: Session, amount_of_fuel: float) -> None:
        ship_crud = ShipRepository(db)
        self.fuel = self.fuel + amount_of_fuel
        ship_crud.update_ship(self)
        print(f"ship {self} refueld ok")


    def load(self, db: Session, container: Container) -> bool:
        #db: Session = Depends(get_db)
        container_crud = ContainerRepository(db)
        container.port_id = None
        container.ship_id = self.id
        container_crud.update_container(container)
        print(f"container {container} load into ship {self}")
        return True

    def unload(self, db: Session, container: Container) -> bool:
        container_crud = ContainerRepository(db)
        container.port_id = self.port_id
        container.ship_id = None
        container_crud.update_container(container)
        print(f"container {container} unload from ship {self}")
        return True


    class Config:
        orm_mode = True


class LightWeightShip(IShip):
    def __repr__(self):
        return f"The ship {self.id} is a lightweight ship."
    pass


class MediumShip(IShip):
    def __repr__(self):
        return f"The ship {self.id}is a medium ship."
    pass


class HeavyShip(IShip):
    def __repr__(self):
        return f"The ship {self.id} is a heavy ship."
    pass


