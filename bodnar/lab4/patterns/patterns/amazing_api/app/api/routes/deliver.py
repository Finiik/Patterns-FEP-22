from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def gett_all_ships() -> List[dict]:
    ships = [
        {"id": 1, "title": "Titanic", "type": "heavyweight", "containers_number": 30},
        {"id": 2, "title": "Britanic", "type": "lightweight", "containers_number": 10}
    ]

    return ships
