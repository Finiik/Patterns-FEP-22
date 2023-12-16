from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, ID: int, weight: float, count: int, item_type: str, containerID: int,
                 specific_attribute: int = 0):
        self.ID = ID
        self.weight = weight
        self.count = count
        self.item_type = item_type
        self.containerID = containerID
        self.specific_attribute = specific_attribute

    @abstractmethod
    def get_total_weight(self) -> float:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} item with ID {self.ID} loaded."

    @staticmethod
    def check_type(id, weight, count, item_type=None, container_id=None, specific_attribute=None):
        if weight <= 150.00 and item_type is None:
            return Small(id, weight, count, "Small", container_id, specific_attribute)
        elif weight > 150.00 and item_type is None:
            return Heavy(id, weight, count, "Heavy", container_id, specific_attribute)
        elif item_type == "Refrigerated":
            return Refrigerated(id, weight, count, "Refrigerated", container_id, specific_attribute)
        elif item_type == "Liquid":
            return Liquid(id, weight, count, "Liquid", container_id, specific_attribute)
        else:
            print(f"Failed to create item of type: {item_type}")
            print(f"Weight: {weight}, Item Type: {item_type}")
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


Item.item_types = {
    'Small': Small,
    'Heavy': Heavy,
    'Refrigerated': Refrigerated,
    'Liquid': Liquid,
}
