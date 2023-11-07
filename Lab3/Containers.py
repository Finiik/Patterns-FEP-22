from abc import ABC, abstractmethod
from uuid import uuid4
import Items

class IContainer(ABC):
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
    def predictWeight(self, item: Items.Item)->float:
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

    def add_item(self, item: Items.Item):
        if isinstance(item, Items.SmallItem) and  self.predictWeight(item) <=self.weight:
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

    def add_item(self, item: Items.Item):
        if isinstance(item,Items.LargeItem) and  self.predictWeight(item) <=self.weight:
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

    def add_item(self, item: Items.Item):
      if isinstance(item, Items.RefrigiratedItem) and  self.predictWeight(item) <=self.weight:
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

    def add_item(self, item: Items.Item):
        if  isinstance(item, Items.LiquidItem) and  self.predictWeight(item) <=self.weight:
            self.items.append(item)
            self.currentweight =self.predictWeight(item)
            print("Loaded")
        else:
            print("Failed to load")

