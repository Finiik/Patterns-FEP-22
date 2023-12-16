from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select

from app.models import models
from app.schemas.containers_ import Container


class ContainerRepository:
    # Implements CRUD (Create, Read, Update and Delete) for port objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_container(self, container: Container) -> models.Container:
        db_container = models.Container(id=container.id,
                                        id_check=container.id_check,
                                        weight_check=container.weight_check,
                                        type_check=container.type_check)
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

    def update_container(self, container: Container) -> models.Container:
        container_update = update(models.Container).where(
            models.Container.id == container.id
        )
        container_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(container_update)
        return container
