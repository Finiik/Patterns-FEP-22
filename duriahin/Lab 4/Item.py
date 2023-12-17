from pydantic import BaseModel
from abc import ABC, abstractmethod
from uuid import uuid4


class IItem(BaseModel, ABC):
    weight: float
    amount: int
    container_id: str
    def __init__(self):
        pass
    def getWeight(self):
        pass
    class Config:
        orm_mode = True

class Item(IItem):
    def __init__(self, weight: float, amount: int, container_id: str):
        self.id=uuid4()
        self.weight = weight
        self.amount = amount
        self.container_id = container_id
    def getWeight(self)->float:
        return self.weight*self.amount


class CreateItem(Item):
    def Create_Item(weight: float, amount: int, type='B'):
        if weight * amount <=100:
            return SmallItem(weight, amount)
        else:
            if type == 'H':
                return LargeItem(weight, amount)
            elif type == 'L':
                return LiquidItem(weight, amount)
            elif type == 'R':
                return RefrigiratedItem(weight, amount)

    pass



class SmallItem(Item):
    def __init__(self,amount, weight):
        self.weight = weight
        self.amount = amount
    def getWeight(self)->float:
        return self.weight * self.amount
    pass


class LargeItem(Item):
    def __init__(self,amount, weight):
        self.weight = weight
        self.amount = amount
    def getWeight(self)->float:
        return self.weight * self.amount
    pass

class RefrigiratedItem(LargeItem):
    def __init__(self,amount, weight):
        self.weight = weight
        self.amount = amount
    def getWeight(self)->float:
        return self.weight * self.amount
    pass

class LiquidItem(LargeItem):
    def __init__(self,amount, weight):
        self.weight = weight
        self.amount = amount
    def getWeight(self)->float:
        return self.weight * self.amount
    pass
