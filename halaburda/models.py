from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Ship(Base):
    __tablename__ = "ships"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    containers = relationship("Container", back_populates="ship")

class Port(Base):
    __tablename__ = "ports"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    containers = relationship("Container", back_populates="port")

class Container(Base):
    __tablename__ = "containers"
    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, ForeignKey("ships.id"))
    port_id = Column(Integer, ForeignKey("ports.id"))
    items = relationship("Item", back_populates="container")
    ship = relationship("Ship", back_populates="containers")
    port = relationship("Port", back_populates="containers")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    container_id = Column(Integer, ForeignKey("containers.id"))
    container = relationship("Container", back_populates="items")

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
