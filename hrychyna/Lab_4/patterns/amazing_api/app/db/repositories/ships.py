from sqlalchemy.orm import Session
from sqlalchemy import update
from app.models import models
from app.schemas.ship import Ship
from sqlalchemy.future import select


class ShipRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_ships(self, ship: Ship) -> models.Ship:
        db_ship = models.Ship(id=ship.id,
                              fuel=ship.fuel,
                              ship_id=ship.ship_id,
                              total_weight_capacity=ship.total_weight_capacity,
                              max_number_of_all_containers=ship.max_number_of_all_containers,
                              max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
                              max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
                              max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
                              fuel_consumption_per_km=ship.fuel_consumption_per_km)
        self.db_session.add(db_ship)
        self.db_session.commit()
        self.db_session.refresh(db_ship)
        return db_ship

    def get_by_id(self, ship_id: int) -> models.Ship:
        ships = self.db_session.execute(
            select(models.Ship).filter(models.Port.id == ship_id)
        )
        return ships.scalars().first()

    def get_all_ships(self):
        ships = self.db_session.execute(select(models.Ship).order_by(models.Ship.id))
        return ships.scalars().all()

    def update_ship(self, ship: Ship) -> models.Ship:
        ship_update = update(models.Ship).where(
            models.Ship.id == ship.id
        )
        ship_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(ship_update)
        return ship
