from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select

from app.models import models
from app.schemas.items_ import Item


class ItemRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_item(self, item: Item) -> models.Item:
        db_item = models.Item(id=item.id,
                              weidht=item.weight,
                              count=item.count,
                              container_id=item.container_id)
        self.db_session.add(db_item)
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return db_item

    def get_by_id(self, item_id: int) -> models.Item:
        item = self.db_session.execute(
            select(models.Item).filter(models.Item.id == item_id)
        )
        return item.scalars().first()

    def get_all_items(self):
        items = self.db_session.execute(select(models.Item).order_by(models.Item.id))
        return items.scalars().all()

    def update_port(self, item: Item) -> models.Item:
        item_update = update(models.Item).where(
            models.Item.id == item.id
        )
        item_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(item_update)
        return item
