# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)


class Ship(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    containers = relationship('Container', back_populates='ship')


class Port(Base):
    __tablename__ = 'ports'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    containers = relationship('Container', back_populates='port')


class Container(Base):
    __tablename__ = 'containers'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    ship_id = Column(Integer, ForeignKey('ships.id'))
    port_id = Column(Integer, ForeignKey('ports.id'))
    ship = relationship('Ship', back_populates='containers')
    port = relationship('Port', back_populates='containers')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
