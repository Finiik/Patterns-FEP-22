# models.py (Bookstore models)
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)


# Other code remains the same in models.py
class Inventory:
    pass


class Order:
    pass
