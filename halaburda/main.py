from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models import Ship, SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_ship/")
def create_ship(ship_name: str, db: Session = Depends(get_db)):
    db_ship = Ship(name=ship_name)
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return {"ship_id": db_ship.id, "ship_name": db_ship.name}
