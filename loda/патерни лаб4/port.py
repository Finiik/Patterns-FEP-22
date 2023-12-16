from abc import ABC, abstractmethod
from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class ContainerDetails:
    basic_cont: int
    heavy_cont: int
    refrigerated_cont: int
    liquid_cont: int


class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, s):
        pass

    def outgoing_ship(self, s):
        pass


class Port(IPort, BaseModel, ABC):
    id: str
    latitude: float
    longitude: float
    data_cont: ContainerDetails
    containers: list = []
    ship_history: list = []
    ship_current: list = []

    # ... (rest of the code remains the same)
