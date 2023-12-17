from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select

from app.models import models
from app.schemas.ship import IShip


class ShipRepository:
    def __init__(self, db_session: Session) ->None:
        self.db_session = db_session


    """
    id: Mapped[int] = mapped_column(primary_key=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    type = Column(String(15), nullable=False, unique=False, index=True)
    fuel = Column(Float, nullable=False, unique=False)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id"))
    port: Mapped["Port"] = relationship(back_populates="ships")"""

    def create_ship(self, ship: IShip) -> models.Ship:
        db_ship = models.Ship(id=ship.id, title=ship.title, type_=ship.type_, fuel=ship.fuel, port_id=ship.port_id,
                              port_deliver_id=ship.port_deliver, total_weight_capacity=ship.total_weight_capacity,
                              max_number_of_all_containers=ship.max_number_of_all_containers,
                              max_number_of_basic_containers=ship.max_number_of_basic_containers,
                              max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
                              max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
                              max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
                              fuel_consumption_per_km=ship.fuel_consumption_per_km)
        self.db_session.add(db_ship)
        self.db_session.commit()
        self.db_session.refresh(db_ship)
        return db_ship

    def get_by_id(self, ship_id: int) -> models.Ship:
        ship = self.db_session.execute(
            select(models.Ship).filter(models.Ship.id == ship_id)
        )
        return ship.scalars().first()

    def get_all_ships(self) -> list[models.Ship]:
        ships = self.db_session.execute(select(models.Ship).order_by(models.Ship.id))
        return ships.scalars().all()

    def update_ship(self, ship: IShip) -> models.Ship:
        ship_update = (update(models.Ship)
        .values(
            title=ship.title, type_=ship.type_, fuel=ship.fuel, port_id=ship.port_id,
            port_deliver_id=ship.port_deliver, total_weight_capacity=ship.total_weight_capacity,
            max_number_of_all_containers=ship.max_number_of_all_containers,
            max_number_of_basic_containers=ship.max_number_of_basic_containers,
            max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
            max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
            max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
            fuel_consumption_per_km=ship.fuel_consumption_per_km
        )
        .where(
            models.Ship.id == ship.id
        ))
        ship_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(ship_update)
        self.db_session.commit()
        return
