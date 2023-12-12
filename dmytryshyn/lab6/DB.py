from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class TableProducts(Base):
    __tablename__ = 'Products'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    product_name = Column("product_name", String)
    amount = Column("amount", Integer)
    price = Column("price", Integer)

    def __init__(self, product_name: str, amount: int, price: int):
        self.product_name = product_name
        self.amount = amount
        self.price = price


class TableCard(Base):
    __tablename__ = "Cards_data"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    card_number = Column("card_number", String)
    balance = Column("balance", Integer)

    def __init__(self, card_number: str, balance: int):
        self.card_number = card_number
        self.balance = balance


class TableProvider(Base):
    __tablename__ = "Providers"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    shipment_price = Column("shipment_price", Integer)

    def __init__(self, name: str, shipment_price: int):
        self.name = name
        self.shipment_price = shipment_price


engine = create_engine("sqlite:///input_data.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()