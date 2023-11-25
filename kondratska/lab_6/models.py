from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    value = Column(Float, nullable=False)


class CardDetails(Base):
    __tablename__ = 'card_details'

    id = Column(Integer, primary_key=True)
    card_number = Column(String, nullable=False)
    expiration_date = Column(String, nullable=False)
    cvv = Column(String, nullable=False)


class ShipmentDetails(Base):
    __tablename__ = 'shipment_details'

    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    weight = Column(Float, nullable=False)


class ShipmentProvider(Base):
    __tablename__ = 'shipment_providers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('card_details.id'))
    card = relationship('CardDetails')


class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    shipment_provider_id = Column(Integer, ForeignKey('shipment_providers.id'))
    shipment_provider = relationship('ShipmentProvider')
    shipment_details_id = Column(Integer, ForeignKey('shipment_details.id'))
    shipment_details = relationship('ShipmentDetails')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String, index=True)
    expiration_date = Column(String)
    cvv = Column(String)
    destination = Column(String)
    weight = Column(Float)
