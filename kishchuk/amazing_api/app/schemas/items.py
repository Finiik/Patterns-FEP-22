from abc import ABC, abstractmethod
from pydantic import BaseModel


class Item(BaseModel, ABC):
    pass