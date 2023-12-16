from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from app.models import models
from app.schemas.port import Port


class PortRepository:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_port(self, port: Port) -> models.Port:
        db_port = models.Port(id=port.id, title=port.title,
                              longitude=port.longitude,
                              latitude=port.latitude)
        self.db_session.add(db_port)
        self.db_session.commit()
        self.db_session.refresh(db_port)
        return db_port

    def get_port_by_id(self, port_id: int) -> models.Port:
        port = self.db_session.execute(
            select(models.Port).filter(models.Port.id == port_id)
        )
        return port.scalars().first()

    def get_all_ports(self):
        ports = self.db_session.execute(select(models.Port).order_by(models.Port.id))
        return ports.scalars().all()

    def update_port(self, port: Port) -> None:
        port_update = update(models.Port).where(models.Port.id == port.id)
        port_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(port_update)

    def delete_port(self, port_id: int) -> None:
        self.db_session.execute(
            delete(models.Port).where(models.Port.id == port_id)
        )
        self.db_session.commit()
