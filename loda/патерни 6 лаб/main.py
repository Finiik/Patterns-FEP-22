# main.py (Bookstore application)
from fastapi import FastAPI
from sqlalchemy import create_engine

from models import Base  # Assuming you have a Book model

app = FastAPI()

engine = create_engine("sqlite:///./bookstore.db")
Base.metadata.create_all(bind=engine)
