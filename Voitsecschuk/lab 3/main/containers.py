from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from uuid import UUID
from item import ItemFactory


@dataclass
class Container(ABC):
    id: UUID
    weight: float
    items: list = field(default_factory=list)

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__(self, other) -> bool:
        if isinstance(other, Container):
            id_check = self.id == other.id
            weight_check = self.weight == other.weight
            type_check = self.__class__ == other.__class__
            return id_check and weight_check and type_check
        return False

    def load_item(self, item_type, ID, weight, count, containerID, specific_attribute):
        factory = ItemFactory()
        item = factory.create_item(item_type, ID, weight, count, containerID, specific_attribute)
        if item:
            self.items.append(item)
            print(f"Loading {item_type} item with ID {ID} into Container {self.id}...")
        else:
            print(f"Invalid item type: {item_type}")

    def unload_item(self, item_id):
        item_to_remove = next((item for item in self.items if item.ID == item_id), None)
        if item_to_remove is not None:
            self.items.remove(item_to_remove)
            print(f"Unloading {type(item_to_remove).__name__} item with ID {item_id} from Container {self.id}...")
        else:
            print(f"Item with ID {item_id} not found in Container {self.id}.")


@dataclass
class BasicContainer(Container):
    def consumption(self) -> float:
        return self.weight * 2.5


@dataclass
class HeavyContainer(Container):
    def consumption(self) -> float:
        return self.weight * 3.0


@dataclass
class RefrigeratedContainer(HeavyContainer):
    def consumption(self) -> float:
        return self.weight * 5.0


@dataclass
class LiquidContainer(HeavyContainer):
    def consumption(self) -> float:
        return self.weight * 4.0
