from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class TablePort(Base):
    __tablename__ = "Ports"

    id = Column("id", String, primary_key=True)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    basic_cont = Column("basic_cont", Integer)
    heavy_cont = Column("heavy_cont", Integer)
    refrigerated_cont = Column("refrigerated_cont", Integer)
    liquid_cont = Column("liquid_cont", Integer)

    def __init__(self, id: str, latitude: float, longitude: float, basic_cont: int, heavy_cont: int,
                 refrigerated_cont: int, liquid_cont: int):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.basic_cont = basic_cont
        self.heavy_cont = heavy_cont
        self.refrigerated_cont = refrigerated_cont
        self.liquid_cont = liquid_cont


class TableShip(Base):
    __tablename__ = "Ships"

    id = Column("id", String, primary_key=True)
    port_id = Column("port_id", String, ForeignKey('Ports.id'))
    ship_type = Column("ship_type", String)
    fuel = Column("fuel", Integer)
    total_weight_capacity = Column("total_weight_capacity", Integer)
    max_all_cont = Column("max_all_cont", Integer)
    max_basic_cont = Column("max_basic_cont", Integer)
    max_heavy_cont = Column("max_heavy_cont", Integer)
    max_refrigerated_cont = Column("max_refrigerated_cont", Integer)
    max_liquid_cont = Column("max_liquid_cont", Integer)
    fuel_consumption_per_km = Column("fuel_consumption_per_km", Integer)

    def __init__(self, id: str, port_id: str, ship_type: str, fuel: int, total_weight_capacity: int, max_all_cont: int,
                 max_basic_cont: int, max_heavy_cont: int, max_refrigerated_cont: int, max_liquid_cont: int,
                 fuel_consumption_per_km: int):
        self.id = id
        self.fuel = fuel
        self.ship_type = ship_type
        self.port_id = port_id
        self.total_weight_capacity = total_weight_capacity
        self.max_all_cont = max_all_cont
        self.max_basic_cont = max_basic_cont
        self.max_heavy_cont = max_heavy_cont
        self.max_refrigerated_cont = max_refrigerated_cont
        self.max_liquid_cont = max_liquid_cont
        self.fuel_consumption_per_km = fuel_consumption_per_km

    port = relationship("TablePort")


class TableContainer(Base):
    __tablename__ = "Containers"

    id = Column("id", String, primary_key=True)
    port_id = Column("port_id", String, ForeignKey('Ports.id'))
    weight = Column("weight", Integer)
    type = Column("type", String, default=None)

    def __init__(self, id: str, port_id: str, weight: int, type=None):
        self.id = id
        self.weight = weight
        self.type = type
        self.port_id = port_id

    port = relationship("TablePort")


class TableItem(Base):
    __tablename__ = "Items"

    id = Column("id", String, primary_key=True)
    container_id = Column("container_id", String, ForeignKey('Containers.id'))
    weight = Column("weight", Integer)
    count = Column("count", Integer)
    type = Column("type", String, default=None)

    def __init__(self, id: str, container_id: str, weight: int, count: int, type=None):
        self.id = id
        self.weight = weight
        self.count = count
        self.type = type
        self.container_id = container_id

    container = relationship("TableContainer")


engine = create_engine("sqlite:///input_data.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()
