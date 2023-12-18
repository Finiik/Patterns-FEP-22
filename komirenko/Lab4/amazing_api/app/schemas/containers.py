from abc import ABC, abstractmethod
from pydantic import BaseModel
import random


class Container(BaseModel, ABC):
    id: int
    weight: float
    port_id: int
    ship_id: int

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__(self, other) -> bool:
        id_check = self.id == other.id
        weight_check = self.weight == other.weight
        type_check = self.__class__ == other.__class__
        if id_check and weight_check and type_check:
            return True
        else:
            return False


class BasicContainer(Container):

    def __repr__(self):
        return f"Basic cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):

    def __repr__(self):
        return f"Heavy cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(Container):

    def __repr__(self):
        return f"Refrigerated cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(Container):

    def __repr__(self):
        return f"Liquid cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 4.0

