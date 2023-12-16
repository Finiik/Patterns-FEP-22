from abc import ABC, abstractmethod
from uuid import UUID
from pydantic import BaseModel


class Item(BaseModel, ABC):
    ID: UUID
    weight: float
    count: int
    item_type: str
    container_id: UUID
    specific_attribute: int = 0

    @abstractmethod
    def get_total_weight(self) -> float:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} item with ID {self.ID} loaded."

    @staticmethod
    def check_type(id, weight, count, item_type=None, container_id=None, specific_attribute=None):
        if weight <= 150.00 and item_type is None:
            return Small(id=id, weight=weight, count=count,
                         item_type="Small", container_id=container_id, specific_attribute=specific_attribute)
        if weight > 150.00 and item_type is None:
            return Heavy(id=id, weight=weight, count=count,
                         item_type="Heavy", container_id=container_id, specific_attribute=specific_attribute)
        if item_type == "Refrigerated":
            return Refrigerated(id=id, weight=weight, count=count,
                                item_type="Refrigerated", container_id=container_id, specific_attribute=specific_attribute)
        if item_type == "Liquid":
            return Liquid(id=id, weight=weight, count=count,
                          item_type="Liquid", container_id=container_id, specific_attribute=specific_attribute)
        return None

    @staticmethod
    def create_item(item_type, ID, weight, count, containerID, specific_attribute):
        item_class = Item.item_types.get(item_type)
        if item_class:
            return item_class(ID, weight, count, item_type, containerID, specific_attribute)
        else:
            raise ValueError(f"Invalid item type: {item_type}")


class Small(Item):
    def get_total_weight(self) -> float:
        specific_attribute = self.specific_attribute or 0
        return self.weight * self.count + specific_attribute


class Heavy(Item):
    def get_total_weight(self) -> float:
        specific_attribute = self.specific_attribute or 0
        return self.weight * self.count + specific_attribute


class Refrigerated(Item):
    def get_total_weight(self) -> float:
        specific_attribute = self.specific_attribute or 0
        return self.weight * self.count + specific_attribute


class Liquid(Item):
    def get_total_weight(self) -> float:
        specific_attribute = self.specific_attribute or 0
        return self.weight * self.count + specific_attribute

