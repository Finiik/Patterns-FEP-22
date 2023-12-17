from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List

from Database.db import Base

class Container(Base):
    __tablename__ = "containers"
    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    port_id = Column(String, ForeignKey("ports.id"))
    ship_id = Column(String, ForeignKey("ships.id"))
    weight = Column(Float, nullable=False)
    current_weight = Column(Float, nullable=False)
    items:  Mapped[List["Item"]] = relationship("Item", backref="container")


class Item(Base):
    __tablename__ = "items"
    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    weight = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    container_id = Column(String, ForeignKey("containers.id"))

class Port(Base):
    __tablename__ = "ports"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    ships: Mapped[List["Ship"]] = relationship(back_populates="ship_id")
    basic = Column(Integer, nullable=False)
    heavy = Column(Integer, nullable=False)
    liquid = Column(Integer, nullable=False)


class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[str] = mapped_column(primary_key=True)
    type = Column(String(15), nullable=False, unique=False, index=True)
    ship_id = relationship(Port, back_populates="ships")
    fuel = Column(Float, nullable=False, unique=False)
    port_id: Mapped[String] = mapped_column(ForeignKey("ports.id"))
    totalWeightCapacity = Column(Float, nullable=False)
    maxNumberOfAllContainers = Column(Integer, nullable=False)
    maxNumberOfHeavyContainers = Column(Integer, nullable=False)
    maxNumberOfRefrigeratedContainers = Column(Integer, nullable=False)
    maxNumberOfLiquidContainers = Column(Integer, nullable=False)
    fuelConsumptionPerKM = Column(Float, nullable=False)
    containers: Mapped[List["Container"]] = relationship("Container", backref="container")

    def __repr__(self):
        return f'Ship(title={self.id})'
