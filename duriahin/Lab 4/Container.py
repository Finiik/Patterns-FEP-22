from abc import ABC, abstractmethod
from pydantic import BaseModel

from abc import ABC, abstractmethod
from uuid import uuid4
from Elements import Item

class IContainer(BaseModel, ABC):
    id: str
    weight: float
    current_weight: float
    items: list[Item.Item] | None = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

    @abstractmethod
    def consumption(self) -> float:
        pass
    def add_item(self, item):
        pass


class Container(IContainer):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight
        self.currentweight = 0
        self.items = []


    def consumption(self) -> float:
        pass
    def add_item(self, item):
        pass

    def __eq__(self, other):
        if other is not None:
            id_check = self.id == other.id
            weight_check = self.weight == other.weight
            type_check = self.__class__ == other.__class__
            if weight_check and type_check and id_check:
                return True
            else:
                return False
        else:
            return False
    def predictWeight(self, item: Item.Item)->float:
        return self.currentweight + item.getWeight()


class CreateContainer(Container):
    @staticmethod
    def create_container(container_type="B", weight=0):
        if weight <= 3000 and container_type == "B":
            return BasicContainer(weight)
        else:
            if container_type == "H":
                return HevyContainer(weight)
            elif container_type == "R":
                return RefrigiratorContainer(weight)
            elif container_type == "L":
                return LiquidContainer(weight)
            else:
                print("Invalid container type")


class BasicContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__( weight)
        self.weight = weight
        self.id = uuid4()

    def consumption(self) -> float:
        return self.currentweight

    def add_item(self, item: Item.Item):
        if isinstance(item, Item.SmallItem) and  self.predictWeight(item) <=self.weight:
            self.items.append(item)
            self.currentweight =self.predictWeight(item)
            print("Loaded")
        else:
            print("Failed to load")


class HevyContainer(Container):
    def __init__(self,  weight: float) -> None:
        super().__init__( weight)
        self.weight = weight
        self.id = uuid4()

    def consumption(self) -> float:
        return self.currentweight

    def add_item(self, item: Item.Item):
        if isinstance(item,Item.LargeItem) and  self.predictWeight(item) <=self.weight:
            self.items.append(item)
            self.currentweight =self.predictWeight(item)
            print("Loaded")
        else:
            print("Failed to load")


class RefrigiratorContainer(HevyContainer):
    def __init__(self,  weight: float) -> None:
        super().__init__( weight)
        self.weight = weight
        self.id = uuid4()

    def consumption(self) -> float:
        return self.currentweight

    def add_item(self, item: Item.Item):
      if isinstance(item, Item.RefrigiratedItem) and  self.predictWeight(item) <=self.weight:
        self.items.append(item)
        self.currentweight =self.predictWeight(item)
        print("Loaded")
      else:
        print("Failed to load")


class LiquidContainer(HevyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__( weight)
        self.weight = weight
        self.id = uuid4()

    def consumption(self) -> float:
        return self.currentweight

    def add_item(self, item: Item.Item):
        if  isinstance(item, Item.LiquidItem) and  self.predictWeight(item) <=self.weight:
            self.items.append(item)
            self.currentweight =self.predictWeight(item)
            print("Loaded")
        else:
            print("Failed to load")

