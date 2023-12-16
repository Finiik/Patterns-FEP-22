from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.item import Item
from app.db.database import get_db
from app.db.repositories.items import ItemRepository

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item, db: Session = Depends(get_db)):
    item_crud = ItemRepository(db_session=db)
    db_item = item_crud.get_by_id(item_id=item.id)
    if db_item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Item already exist"
        )
    db_item = item_crud.create_item(item=item)
    return db_item


@router.get("/", response_model=list[Item], status_code=status.HTTP_200_OK)
def get_all_items(db: Session = Depends(get_db)):
    item_crud = ItemRepository(db_session=db)
    return item_crud.get_all_items()
