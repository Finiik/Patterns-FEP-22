from abc import ABC, abstractmethod
from uuid import uuid4


# новий клас
class Item(ABC):  # абстрактний клас
    def __init__(self, weight: float, count: int, container_id):
        self.ID = uuid4()
        self.weight = weight
        self.count = count
        self.containerID = container_id

    @abstractmethod
    def get_total_weight(self) -> float:
        pass


# підкласи Small, Heavy, Refrigerated, Liquid, які успадковуються від Item
class Small(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count


class Heavy(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count


class Refrigerated(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count


class Liquid(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count


# фабрика для створення контейнерів різних типів
class ItemFactory:
    @staticmethod
    def create_item(item_type, weight, count, container_id):
        if item_type == "Small":
            return Small(weight, count, container_id)
        elif item_type == "Heavy":
            return Heavy(weight, count, container_id)
        elif item_type == "Refrigerated":
            return Refrigerated(weight, count, container_id)
        elif item_type == "Liquid":
            return Liquid(weight, count, container_id)


# використання фабрики для створення об'єктів Small, Heavy, Refrigerated, Liquid
small_item = ItemFactory.create_item("Small", 10.0, 5, "S111")
heavy_item = ItemFactory.create_item("Heavy", 20.0, 3, "H222")
refrigerator_item = ItemFactory.create_item("Refrigerated", 15.0, 2, "R333")
liquid_item = ItemFactory.create_item("Liquid", 12.0, 4, "L444")
# кінець нового класу


class Container(ABC):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight

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
    def __init__(self, weight: float) -> None:
        Container.__init__(self, weight=weight)

    def consumption(self) -> float:
        return self.weight * 2.5  # повертає споживання пального, розраховане відповідно до вказаних коефіцієнтів


class HeavyContainer(Container):
    def __init__(self, weight: float) -> None:
        Container.__init__(self, weight=weight)

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        HeavyContainer.__init__(self, weight=weight)

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        HeavyContainer.__init__(self, weight=weight)

    def consumption(self) -> float:
        return self.weight * 4.0
