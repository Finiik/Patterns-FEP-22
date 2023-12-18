from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Union
from pydantic import BaseModel
from item import Item


class Container(BaseModel, ABC):

    container_id: str
    weight: float
    items: List[Item]
    max_items: int = 2

    @abstractmethod
    def consumption(self) -> float:
        pass

    @staticmethod
    def create_container(container_id: str, weight: float, container_type: str) -> Container:
        if weight <= 3000:
            return BasicContainer(container_id=container_id, weight=weight, container_type="Basic")
        elif weight > 3000 and container_type is None:
            return HeavyContainer(container_id=container_id, weight=weight, container_type="Heavy")
        elif container_type == "R":
            return RefrigeratedContainer(container_id=container_id, weight=weight, container_type="Refrigerated")
        elif container_type == "L":
            return LiquidContainer(container_id=container_id, weight=weight, container_type="Liquid")

    def __str__(self) -> str:
        item_info = '\n'.join([f"Item: {item['item_type']}, Weight: {item['weight']}" for item in self.items])
        return f"Type: {self.__class__.__name__}\nWeight: {self.weight}\nID: {self.id}\nItems: {item_info}"

    def load_item(self, item_type: str, item_id: str, weight: float, count: int, specific_attribute: float) -> None:
        item = {
            "item_type": item_type,
            "ID": item_id,
            "weight": weight,
            "count": count,
            "specific_attribute": specific_attribute
        }
        self.items.append(item)

    def unload_item(self, item_id: UUID) -> Union[None, dict]:
        for i, item in enumerate(self.items):
            if item["ID"] == item_id:
                return self.items.pop(i)
        return None


class BasicContainer(Container):
    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):
    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):
    def consumption(self) -> float:
        return self.weight * 4.0


class ContainerDetails:
    def __init__(self, basic_containers: List[Container], heavy_containers: List[Container],
                 refrigerated_containers: List[Container], liquid_containers: List[Container]) -> None:
        self.basic_containers = basic_containers
        self.heavy_containers = heavy_containers
        self.refrigerated_containers = refrigerated_containers
        self.liquid_containers = liquid_containers


def get_type(container):
    if isinstance(container, BasicContainer):
        return container.id
    elif isinstance(container, HeavyContainer):
        return container.id
    elif isinstance(container, RefrigeratedContainer):
        return container.id
    elif isinstance(container, LiquidContainer):
        return container.id

