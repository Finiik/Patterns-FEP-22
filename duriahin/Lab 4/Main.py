from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from sqlalchemy.orm import Session
import sys

import crud

sys.path.insert(1, r'E:\Paterns\Provided example\patterns-main\amazing_api\app\api')
sys.path.insert(1, r'E:\Paterns\Provided example\patterns-main\amazing_api\app\db')
from Model import models
from crud import *
from Elements import Port, Ship, Container, Item
from Database.db import Base, engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/port/", response_model=Port.Port)
def create_port(config_port_json: Port.Port, db: Session = Depends(get_db)):
    db_user = crud.get_port(db, config_port_json.port_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Port already exists")
    return crud.create_port(db=db, config_port=config_port_json)


@app.get("/port/", response_model=list[Port.Port])
def get_ports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ports = crud.get_ports(db, skip, limit)
    return ports


@app.get("/port/{port_id}", response_model=Port.Port)
def get_port(port_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_port(db, port_id=port_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Port not found")
    return db_user



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
