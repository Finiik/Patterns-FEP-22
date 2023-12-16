from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from app.models import models
from app.schemas.ship import IShip


class ShipRepository:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_ship(self, ship) -> IShip:
        db_ship = models.Ship(
            id=ship.id,
            title=ship.title,
            type=ship.type,
            fuel=ship.fuel,
            total_weight_capacity=ship.total_weight_capacity,
            max_number_of_all_containers=ship.max_number_of_all_containers,
            max_number_of_basic_containers=ship.max_number_of_basic_containers,
            max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
            max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
            max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
            fuel_consumption_per_km=ship.fuel_consumption_per_km,
            port_id=ship.port_id,
        )
        self.db_session.add(db_ship)
        self.db_session.commit()
        self.db_session.refresh(db_ship)
        return db_ship

    def get_ship_by_id(self, ship_id: int):
        ship = self.db_session.execute(
            select(models.Ship).filter(models.Ship.id == ship_id)
        )
        return ship.scalars().first()

    def get_all_ships(self):
        ships = self.db_session.execute(select(models.Ship).order_by(models.Ship.id))
        return ships.scalars().all()

    def delete_ship(self, ship_id: int) -> None:
        self.db_session.execute(
            delete(models.Ship).where(models.Ship.id == ship_id)
        )
        self.db_session.commit()
