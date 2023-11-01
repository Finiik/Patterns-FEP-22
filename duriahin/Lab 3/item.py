from abc import ABC, abstractmethod
from typing import Union

class Item(ABC):
    def __init__(self, ID: int, weight: float, count: int, containerID: int, specific_attribute: float):
        self.ID = ID
        self.weight = weight
        self.count = count
        self.containerID = containerID
        self.specific_attribute = specific_attribute

    @abstractmethod
    def get_total_weight(self) -> float:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} item with ID {self.ID} loaded."


class Small(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count + self.specific_attribute


class Heavy(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count + self.specific_attribute


class Refrigerated(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count + self.specific_attribute


class Liquid(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count + self.specific_attribute


class ItemFactory:
    @staticmethod
    def create_item(item_type: str, ID: int, weight: float, count: int, containerID: int, specific_attribute: float) -> Union[Small, Heavy, Refrigerated, Liquid]:
        if item_type == 'Small':
            return Small(ID, weight, count, containerID, specific_attribute)
        elif item_type == 'Heavy':
            return Heavy(ID, weight, count, containerID, specific_attribute)
        elif item_type == 'Refrigerated':
            return Refrigerated(ID, weight, count, containerID, specific_attribute)
        elif item_type == 'Liquid':
            return Liquid(ID, weight, count, containerID, specific_attribute)
        else:
            raise ValueError(f"Invalid item type: {item_type}")
