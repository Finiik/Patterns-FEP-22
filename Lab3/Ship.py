from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4
import geopy.distance
from Containers import *

@dataclass
class ConfigShip:
        ship_id: str
        port_id: str
        ports_deliver: str
        totalWeightCapacity: int
        maxNumberOfAllContainers: int
        maxNumberOfHeavyContainers: int
        maxNumberOfRefrigeratedContainers: int
        maxNumberOfLiquidContainers: int
        fuelConsumptionPerKM: int


class IShip(ABC):
    @abstractmethod
    def sail_to(self, port, other_port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel:float) -> None:
        pass

    @abstractmethod
    def load(self, container, port) -> bool:
        pass

    @abstractmethod
    def unload(self, container, port) -> bool:
        pass

class AbstractShipFactory(ABC):
    @abstractmethod
    def create_ship( config_ship: ConfigShip):
        pass

class LightWeightSHipFactory(AbstractShipFactory):
    def create_ship( config_ship: ConfigShip):
        return LightWeightShip(config_ship)

class MediumShipFactory(AbstractShipFactory):
    def create_ship( config_ship: ConfigShip):
        return MediumWeightShip(config_ship)
class HeavyShipFactory(AbstractShipFactory):
    def create_ship( config_ship: ConfigShip):
        return HeavyWeightShip(config_ship)


class Ship(IShip):
    def __init__(self, ship_config: ConfigShip)->None:
        self.ship_config = ship_config
        self.containers = []
        self.current_weight = 0
        self.fuel = 100000
        self.max_fuel = 100000

    def get_amount_of_heavy_containers(self) -> int:
        amount = 0
        for container in self.containers:
            if type(container) == HevyContainer:
                amount += 1
        return amount

    def get_amount_of_basic_containers(self) -> int:
        amount = 0
        for container in self.containers:
            if type(container.container) == BasicContainer:
                amount += 1
        return amount

    def get_weight(self):
        return self.ship_config.totalWeightCapacity

    def get_id(self):
        return self.ship_config.ship_id

    def get_amount_of_liquid_containers(self) -> int:
        amount = 0
        for container in self.containers:
            if type(container) == LiquidContainer:
                amount += 1
        return amount

    def get_amount_of_refrigirator_containers(self) -> int:
        amount = 0
        for container in self.containers:
            if type(container) == RefrigiratorContainer:
                amount += 1
        return amount

    def get_current_container(self) -> list:
        return self.containers

    def count_fuel_consumption(self) -> float:
            fuel_sum = 0.0
            for container in self.containers:
                fuel_sum += container.consumption()
            fuel_sum += self.ship_config.fuelConsumptionPerKM
            return fuel_sum

    def sail_to(self, this_port , other_port):
        fuel_per_km = self.count_fuel_consumption()
        distance = this_port.get_distance(other_port)
        total_fuel_consuption = distance*fuel_per_km
        if total_fuel_consuption > self.fuel:
            print("Not enough fuel to sail there")
        else:
            this_port.outgoing_ship(self)
            other_port.incoming_ship(self)
            self.fuel -= total_fuel_consuption
            print("Sailed successfully")

    def refuel(self, amount_of_fuel: float) -> bool:
        if self.fuel < self.max_fuel:
            if (self.fuel+amount_of_fuel) > self.max_fuel:
                print("This is too much")
                return False
            else:
                self.fuel += amount_of_fuel
                return True
        else:
            print("This ship don`t need to be refuled")
            return False

    def load(self, container, port):
        if self.check_container_requirements(container):
            if port.give_container(container):
                self.containers.append(container)
                self.current_weight += container.consumption()
                print(f"Container {container.id} succesfully loaded on the ship {self.ship_config.ship_id}")
        else:
            print(f"Ship {self.ship_config.ship_id} filed to load container {container.id} on board")

    def check_container_requirements(self, container: Container) -> bool:
        if len(self.containers) == self.ship_config.maxNumberOfAllContainers:
            print("There is already maximum containers on this ship")
            return False
        elif self.ship_config.totalWeightCapacity <= self.current_weight:
            return False
        else:
            if isinstance(container, HevyContainer):
                if self.get_amount_of_heavy_containers() == self.ship_config.maxNumberOfHeavyContainers:
                    print("There is already maximum amount of heavy containers on this ship")
                    return False
                else:
                    return True
            elif isinstance(container, RefrigiratorContainer):
                if self.get_amount_of_refrigirator_containers() == self.ship_config.maxNumberOfRefrigeratedContainers:
                    print("There is already maximum amount of refrigirator containers on this ship")
                    return False
                else:
                    return True
            elif isinstance(container, LiquidContainer):
                if self.get_amount_of_liquid_containers() == self.ship_config.maxNumberOfLiquidContainers:
                    print("There is already maximum amount of liquid containers on this ship")
                    return False
                else:
                    return True
            else:
                return True
    def get_container(self, container_id):
        container = any(x.id == container_id for x in self.containers)
        if container != None:
            return container
        else:
            return None
    def unload(self, container_id, port):
        container = self.get_container(container_id)
        if container != None:
            port.get_container(container)
            print(f"Container {container.id} was successfully unloaded to the port {port.config_port.port_id}")
            self.containers.remove(container)
        else:
            print(f"Failed to unload container {container.id} to port {port.config_port.port_id}")

    # def count_distance_between_ports(self, this_port, other_port) -> float:
    #     if this_port.port_id == self.ship_config.port_id:
    #         return this_port.get_distance(other_port)
    #     else:
    #         print("This ship is not in this port")
    #         return

class LightWeightShip(Ship):
    def __init__(self, configurateShip: ConfigShip):
        super().__init__(configurateShip)
        self.fuel=1000
        self.max_fuel=1000
    def get_id(self):
        return self.ship_config.ship_id


class MediumWeightShip(Ship):
    def __init__(self, configurateShip: ConfigShip):
        super().__init__(configurateShip)
        self.fuel=10000
        self.max_fuel=10000
    def get_id(self):
        return self.ship_config.ship_id

class HeavyWeightShip(Ship):
    def __init__(self, configurateShip: ConfigShip):
        super().__init__(configurateShip)
        self.fuel=10000
        self.max_fuel=10000
    def get_id(self):
        return self.ship_config.ship_id

