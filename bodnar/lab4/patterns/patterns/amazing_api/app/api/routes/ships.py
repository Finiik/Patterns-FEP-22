from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.ship import Ship
from app.db.database import get_db
from app.db.repositories.ships import ShipRepository

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Ship, status_code=status.HTTP_201_CREATED)
def create_ship(ship: Ship, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    db_ship = ship_crud.get_by_id(ship_id=ship.id)
    if db_ship:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ship already exist"
        )
    db_ship = ship_crud.create_ships(ship=ship)
    return db_ship


@router.get("/", response_model=list[Ship], status_code=status.HTTP_200_OK)
def get_all_ships(db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    return ship_crud.get_all_ships()
