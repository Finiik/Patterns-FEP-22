from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select

from app.models import models
from app.schemas.port import Port


class PortRepository:
    # Implements CRUD (Create, Read, Update and Delete) for port objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_port(self, port: Port) -> models.Port:
        db_port = models.Port(id=port.id, title=port.title,
                         longitude=port.longitude,
                         latitude=port.latitude, basic=port.basic,
                              heavy=port.heavy,refrigerated=port.refrigerated,
                              liquid=port.liquid)
        self.db_session.add(db_port)
        self.db_session.commit()
        self.db_session.refresh(db_port)
        return db_port

    def get_by_id(self, port_id: int) -> models.Port:
        port = self.db_session.execute(
            select(models.Port).filter(models.Port.id == port_id)
        )
        return port.scalars().first()

    def get_all_ports(self):
        ports = self.db_session.execute(select(models.Port).order_by(models.Port.id))
        return ports.scalars().all()

    def update_port(self, port: Port) -> models.Port:
        port_update = (update(models.Port)
        .values(title="New title", basic=100)
        .where(
            models.Port.id == port.id
        ))
        print(f"update_port port = {port}")
        print(f"update_port = {port_update}")
        port_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(port_update)
        self.db_session.commit()
        return
