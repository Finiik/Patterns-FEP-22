from sqlalchemy.orm import Session
from Model import models
from Elements import Ship, Port, Container, Item


def get_port(db:Session, port_id: str):
    return db.query(models.Port).filter(models.Port.id == port_id).first()

def get_ports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Port).offset(skip).limit(limit).all()

def get_ship(db: Session, ship_id):
    return db.query(models.Ship).filter(models.Ship.id == ship_id).firt()

def get_ships_in_port(db: Session, port_id):
    return db.query(models.Ship).filter(models.Ship.port_id == port_id).all()

def create_port(db: Session, config_port):
    db_port = models.Port(id=config_port.port_id, longitude=config_port.longitude, latitude=config_port.latitude, ships=config_port.ships, basic=config_port.basic,heavy=config_port.heavy, liquid=config_port.liquid)
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port
