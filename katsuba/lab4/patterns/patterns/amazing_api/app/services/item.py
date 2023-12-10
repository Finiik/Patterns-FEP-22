from abc import ABC, abstractmethod
from uuid import uuid4


class Item(ABC):
    def __init__(self, weight: float, count: int, container_id):
        self.ID = uuid4()
        self.weight = weight
        self.count = count
        self.containerID = container_id

    @abstractmethod
    def get_total_weight(self) -> float:
        pass


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


small_item = ItemFactory.create_item("Small", 10.0, 5, "S111")
heavy_item = ItemFactory.create_item("Heavy", 20.0, 3, "H222")
refrigerator_item = ItemFactory.create_item("Refrigerated", 15.0, 2, "R333")
liquid_item = ItemFactory.create_item("Liquid", 12.0, 4, "L444")
