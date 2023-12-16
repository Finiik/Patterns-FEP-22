from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List

from app.db.database import Base

'''
class Container(Base):
    __tablename__ = "containers"


class Item(Base):
    __tablename__ = "items"
'''


class Port(Base):
    __tablename__ = "ports"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    ships: Mapped[List["Ship"]] = relationship('Ship', back_populates="port")

    def __repr__(self):
        return (f'Port(id={self.id}, title={self.title}, longitude={self.longitude}, latitude={self.latitude}, '
                f'ships={self.ships}')


class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    port_id = Column(Integer, ForeignKey('ports.id'))
    port = relationship('Port', back_populates='ships')
    title = Column(String(80), nullable=False, unique=True, index=True)
    type = Column(String(15), nullable=False, unique=False, index=True)
    fuel = Column(Float, nullable=False, unique=False)
    total_weight_capacity = Column(Integer, nullable=False, unique=False)
    max_number_of_all_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_basic_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_heavy_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_refrigerated_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_liquid_containers = Column(Integer, nullable=False, unique=False)
    fuel_consumption_per_km = Column(Integer, nullable=False, unique=False)

    def __repr__(self):
        return (f'Ship(id={self.id}, title={self.title}, type={self.type}, fuel={self.fuel}, port_id={self.port_id}, '
                f'port={self.port})')
