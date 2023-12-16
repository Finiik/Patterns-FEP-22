from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List

from app.db.database import Base


class Container(Base):
    __tablename__ = "containers"
    id: Mapped[int] = mapped_column(primary_key=True)
    weight = Column(Float, nullable=False)
    port_id: Mapped[int] = Column(Integer, ForeignKey('ports.id'))
    port: Mapped["Port"] = relationship("Port", back_populates="containers")


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    weight = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)
    container_id: Mapped[int] = Column(Integer, ForeignKey("containers.id"))
    container: Mapped[Container] = relationship("Container", back_populates="items")


class Port(Base):
    __tablename__ = "ports"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    ships: Mapped[List["Ship"]] = relationship(back_populates="port")  # один порт може мати багато суден
    containers: Mapped[List["Container"]] = relationship("Container", back_populates="port")
    items: Mapped[List["Item"]] = relationship("Item", secondary="containers", back_populates="container")


class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(primary_key=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    type = Column(String(15), nullable=False, unique=False, index=True)
    fuel = Column(Float, nullable=False, unique=False)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id"))  # кожне судно має один порт
    port: Mapped["Port"] = relationship(back_populates="ships")

    def __repr__(self):
        return f'Ship(title={self.title})'
