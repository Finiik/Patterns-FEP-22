from abc import ABC, abstractmethod
from pydantic import BaseModel


class Container(BaseModel, ABC):
    pass
