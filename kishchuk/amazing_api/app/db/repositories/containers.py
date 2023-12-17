from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select

from app.models import models
from app.schemas.containers import Container, BasicContainer, HeavyContainer, LiquidContainer, RefrigeratedContainer


class ContainerRepository:
    # Implements CRUD (Create, Read, Update and Delete) for container objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
        print(f"self.db_session = {self.db_session}")


    def create_container(self, container:Container) -> models.Container:
        type = ""
        if isinstance(container, BasicContainer):
            type = "basic"
        elif isinstance(container, HeavyContainer):
            type = "heavy"
        elif isinstance(container, RefrigeratedContainer):
            type = "refrigerated"
        elif isinstance(container, LiquidContainer):
            type = "liquid"
        else:
            raise Exception("unknown container type")

        print(f"container type - {type}")

        if container.port_id == -1:
            port_id = None
        else:
            port_id = container.port_id

        if container.ship_id == -1:
            ship_id = None
        else:
            ship_id = container.ship_id

        db_container = models.Container(id=container.id,type=type, weight=container.weight,
                                        port_id=port_id, ship_id=ship_id)
        self.db_session.add(db_container)
        self.db_session.commit()
        self.db_session.refresh(db_container)
        return db_container

    def get_by_id(self, container_id: int) -> models.Container:
        container = self.db_session.execute(
            select(models.Container).filter(models.Container.id == container_id)
        )
        return container.scalars().first()


    def get_all_containers(self):
        containers = self.db_session.execute(select(models.Container).order_by(models.Container.id))
        return containers.scalars().all()


    def get_containers_by_port(self, port_id:int ):
        containers = self.db_session.execute(select(models.Container)
                                             .where(models.Container.port_id == port_id)
                                             .order_by(models.Container.id))
        return containers.scalars().all()

    def get_containers_by_ship(self, ship_id:int ):
        containers = self.db_session.execute(select(models.Container)
                                             .where(models.Container.ship_id == ship_id)
                                             .order_by(models.Container.id))
        return containers.scalars().all()

    def update_container(self, cont: Container) -> models.Container:
        cont_update = (update(models.Container)
        .values(
            weight=cont.weight,
            port_id=cont.port_id,
            ship_id=cont.ship_id
        )
        .where(
            models.Container.id == cont.id
        ))

        cont_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(cont_update)
        self.db_session.commit()
        return

