from abc import ABC, abstractmethod
from typing import List
#import haversine as hs
from pydantic import BaseModel

# from app.schemas.items import Item
# from app.schemas.containers import Container

class PersonalInfo():
    first_name:str
    second_name:str
    age:int

