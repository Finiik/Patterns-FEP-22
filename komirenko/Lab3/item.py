from abc import ABC, abstractmethod
from uuid import uuid4

class ItemBuilder:

    def __init__(self):
        self._weight = None
        self._count = None
        self._containerID = None
        self._color = None

    def weight(self, weight: float):
        self._weight = weight
        return self

    def count(self, count):
        self._count = count
        return self

    def containerID(self, containerID):
        self._containerID = containerID
        return self

    def color(self, color):
        self._color = color
        return self

    def build(self, item_type):
        if item_type == 'Small':
            return Small(self)
        elif item_type == 'Heavy':
            return Heavy(self)
        elif item_type == 'Refrigerated':
            return Refrigerated(self)
        elif item_type == 'Liquid':
            return Liquid(self)
        else:
            raise ValueError(f"Invalid item type: {item_type}")

class Item(ABC):
    def __init__(self, itemBuilder: ItemBuilder):
        self.ID = int(uuid4())
        self.weight = itemBuilder.weight
        self.count = itemBuilder.count
        self.containerID = itemBuilder.containerID
        self.color = itemBuilder.color

    @abstractmethod
    def get_total_weight(self):
        pass


class Small(Item):
    def __init__(self, itemBuilder: ItemBuilder):
        super().__init__(itemBuilder)

    def __repr__(self):
        return f"Small item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        return f"Total weight of this item is {total_weight}"

class Heavy(Item):
    def __init__(self, itemBuilder: ItemBuilder):
        super().__init__(itemBuilder)

    def __repr__(self):
        return f"Heavy item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        return f"Total weight of this item is {total_weight}"

class Refrigerated(Item):
    def __init__(self, itemBuilder: ItemBuilder):
        super().__init__(itemBuilder)

    def __repr__(self):
        return f"Refrigerated item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        return f"Total weight of this item is {total_weight}"

class Liquid(Item):
    def __init__(self, itemBuilder: ItemBuilder):
        super().__init__(itemBuilder)

    def __repr__(self):
        return f"Liquid item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        return f"Total weight of this item is {total_weight}"
