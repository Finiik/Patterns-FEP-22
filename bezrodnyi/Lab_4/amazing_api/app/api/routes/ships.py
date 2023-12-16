from typing import List, Union, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.schemas.ship import IShip, LightWeightShip, MediumWeightShip, HeavyWeightShip
from app.db.database import get_db
from app.models.models import Ship
from app.db.repositories.ships import ShipRepository

from app.services.ship_service import ShipCreator

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Union[LightWeightShip, MediumWeightShip, HeavyWeightShip],
             status_code=status.HTTP_201_CREATED)
def create_ship(ship_data: Dict[str, Any], db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    ship_db = ship_crud.get_ship_by_id(ship_id=ship_data["id"])
    if ship_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ship already exist"
        )
    ship = ShipCreator().create_ship(ship_data)
    print(ship)
    ship_db = ship_crud.create_ship(ship=ship)
    return ship_db


@router.get("/", response_model=list[Union[LightWeightShip, MediumWeightShip, HeavyWeightShip]],
            status_code=status.HTTP_200_OK)
def get_all_ships(db: Session = Depends(get_db)) -> List[dict]:
    ship_crud = ShipRepository(db_session=db)
    return ship_crud.get_all_ships()
