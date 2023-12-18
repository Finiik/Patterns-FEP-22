from abc import ABC, abstractmethod
from pydantic import BaseModel
from haversine import haversine as hs
from dataclasses import dataclass

@dataclass
class ContainersDetails:
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


class Port(IPort, BaseModel):
    id: str
    latitude: float
    longitude: float
    data_cont: ContainersDetails
    containers: list = []
    ship_history: list = []
    ship_current: list = []

    def get_distance(self, other_port: 'Port') -> float:
        coordinates_self = (self.latitude, self.longitude)
        coordinates_other = (other_port.latitude, other_port.longitude)
        dist = hs.haversine(coordinates_self, coordinates_other)
        return dist

    def incoming_ship(self, s):
        current_id_found = any(obj.id == s.id for obj in self.ship_current)
        if not current_id_found:
            self.ship_current.append(s)

    def outgoing_ship(self, s):
        history_id_found = any(obj.id == s.id for obj in self.ship_history)
        current_id_found = any(obj.id == s.id for obj in self.ship_current)
        if not history_id_found:
            self.ship_history.append(s)
            if current_id_found:
                self.ship_current.remove(s)
