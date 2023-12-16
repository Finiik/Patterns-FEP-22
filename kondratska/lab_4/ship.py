from dataclasses import dataclass
from pydantic import BaseModel
from port import Port
from abc import ABC, abstractmethod
from typing import List, Optional
from container import Container

@dataclass
class ConfigShip:
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: int


class IShip(ABC):
    @abstractmethod
    def sail_to(self, p1, p2, p3):
        pass

    @abstractmethod
    def re_fuel(self, new_fuel: float):
        pass

    @abstractmethod
    def load(self, cont):
        pass

    @abstractmethod
    def unload(self, cont):
        pass


class Ship(IShip, BaseModel):
    id: str
    fuel: float
    current_port: 'Port'
    ships_data: ConfigShip
    ship_type: str
    containers: Optional[List[Container]] = None
    total_weight: int = 0
    total_containers_types: Optional[List] = None
    total_containers_consumption: int = 0
    items: Optional[List] = None

    def __init__(self, id: str, fuel: float, current_port: 'Port', ships_data: ConfigShip, ship_type: str, containers: Optional[List] = None):
        super().__init__(id=id, fuel=fuel, current_port=current_port, ships_data=ships_data, containers=containers)
        self.containers = containers or []
        self.total_containers_types = []
        self.items = []

    def get_current_containers(self):
        if self.containers:
            return [container.id for container in self.containers]
        else:
            return 'There are no containers on the ship'

    def check_current_id(self, port):
        id_found = any(ship.id == self.id for ship in port.ship_current)
        return id_found

    def check_history_id(self, port):
        id_found = any(ship.id == self.id for ship in port.ship_history)
        return id_found

    def sail_to(self, *ports):
        p1, p2, p3 = ports
        total_fuel_needed1 = (self.ships_data.fuel_consumption_per_km * p1.get_distance(p2) +
                              self.total_containers_consumption)
        if self.check_current_id(p1) and total_fuel_needed1 <= self.fuel:
            if not self.check_history_id(p1):
                p1.outgoing_ship(self)
            p2.incoming_ship(self)
            self.fuel -= total_fuel_needed1
            self.current_port = p2
            return 'Ship has successfully sailed to another port'

        elif not self.check_current_id(p1):
            return 'There is no such ship in this port'

        elif self.check_current_id(p1) and total_fuel_needed1 > self.fuel:
            total_fuel_needed2 = self.ships_data.fuel_consumption_per_km * p1.get_distance(
                p3) + self.total_containers_consumption
            if total_fuel_needed2 <= self.fuel:
                if not self.check_history_id(p1):
                    p1.outgoing_ship(self)
                p3.incoming_ship(self)
                self.fuel -= total_fuel_needed2
                total_fuel_needed1 = self.ships_data.fuel_consumption_per_km * p3.get_distance(
                    p2) + self.total_containers_consumption
                while self.fuel < total_fuel_needed1:
                    self.re_fuel(100)
                if not self.check_history_id(p3):
                    p3.outgoing_ship(self)
                p2.incoming_ship(self)
                self.fuel -= total_fuel_needed1
                self.current_port = p2
                return 'Ship has successfully sailed to intermediate port to refuel and sailed to wanted port'

            elif total_fuel_needed2 > self.fuel:
                while self.fuel < total_fuel_needed1:
                    self.re_fuel(100)
                if not self.check_history_id(p1):
                    p1.outgoing_ship(self)
                p2.incoming_ship(self)
                self.fuel -= total_fuel_needed1
                self.current_port = p2
                return 'Ship has successfully sailed to another port after refueling in the starting port'

    def re_fuel(self, new_fuel: float):
        self.fuel += new_fuel

    def load(self, cont):
        max_counts = {
            'Basic': self.ships_data.max_number_of_basic_containers,
            'Heavy': self.ships_data.max_number_of_heavy_containers,
            'Refrigerated': self.ships_data.max_number_of_refrigerated_containers,
            'Liquid': self.ships_data.max_number_of_liquid_containers,
        }
        found_cont_in_port = any(obj.id == cont.id for obj in self.current_port.containers)
        found_cont_on_ship = any(obj.id == cont.id for obj in self.containers)
        if found_cont_in_port:
            if (len(self.containers) < self.ships_data.max_number_of_all_containers
                    and not found_cont_on_ship):
                self.containers.append(cont)
                self.total_weight += cont.weight
                self.total_containers_consumption += cont.consumption()
                self.total_containers_types.append(cont.type)
                self.current_port.containers.remove(cont)
                if all(self.total_containers_types.count(container_type) <= max_count
                       for container_type, max_count in max_counts.items()):
                    if self.total_weight < self.ships_data.total_weight_capacity:
                        return f"{cont.type} container has been loaded on the ship"
                    else:
                        self.containers.remove(cont)
                        self.total_weight -= cont.weight
                        self.total_containers_consumption -= cont.consumption()
                        self.total_containers_types.remove(cont.type)
                        self.current_port.containers.append(cont)
                        return f"{cont.type} container hasn't been loaded on the ship: max weight cap reached"
                else:
                    self.containers.remove(cont)
                    self.total_weight -= cont.weight
                    self.total_containers_consumption -= cont.consumption()
                    self.total_containers_types.remove(cont.type)
                    self.current_port.containers.append(cont)
                    return (f"{cont.type} container hasn't been loaded on the ship: max amount "
                            f"of {cont.type} containers was reached")
            else:
                return f"{cont.type} container hasn't been loaded on the ship: max amount of all containers was reached"
        else:
            return False

    def unload(self, cont):
        found_cont_on_ship = any(obj.id == cont.id for obj in self.containers)
        if found_cont_on_ship:
            self.containers.remove(cont)
            self.current_port.containers.append(cont)
            self.total_weight -= cont.weight
            self.total_containers_consumption -= cont.consumption()
            self.total_containers_types.remove(cont.type)
            return f"{cont.type} container has been unloaded from the ship"
        else:
            return f"failed to unload {cont.id}"

    @staticmethod
    def check_type(id: str, fuel: float, current_port, ships_data: ConfigShip):
        if ships_data.total_weight_capacity <= 20000:
            return LightWeightShip(id=id, fuel=fuel, current_port=current_port, ships_data=ships_data,
                                   ship_type="Light")
        elif ships_data.total_weight_capacity <= 40000:
            return MediumShip(id=id, fuel=fuel, current_port=current_port, ships_data=ships_data, ship_type="Medium")
        elif ships_data.total_weight_capacity <= 60000:
            return HeavyShip(id=id, fuel=fuel, current_port=current_port, ships_data=ships_data, ship_type="Heavy")


class LightWeightShip(Ship):
    ship_type: str


class MediumShip(Ship):
    ship_type: str


class HeavyShip(Ship):
    ship_type: str
