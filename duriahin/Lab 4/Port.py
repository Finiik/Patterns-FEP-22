from pydantic import BaseModel, ConfigDict

from Elements.Ship import Ship
import geopy.distance
from Elements.Container import CreateContainer
from Elements import Container

class Port(BaseModel):
    port_id: str
    longitude: float
    latitude: float
    ships: list[Ship]
    basic: int
    heavy: int
    liquid: int
    def get_distance(self, other_port) -> float:
        if self.port_id != other_port.port_id:
            coord1 = (self.config_port.longitude, self.config_port.latitude)
            coord2 = (other_port.longtitude, other_port.latitude)
            return geopy.distance.geodesic(coord1, coord2).km
        else:
            print("This ship is already in the port {}".format(self.port_id))

    def incoming_ship(self, ship: Ship):
        if isinstance(ship, Ship) and ship not in self.config_port.ships:
            self.config_port.ships.append(ship)
        return True

    def outgoing_ship(self, ship: Ship):
        self.ship_history.append(ship)
        self.config_port.ships.remove(ship)
        return False

    def get_ships(self):
        for i in self.ships:
            print(f"Ship {i.get_id()} is in port {self.port_id}")

    def create_container(self, mode="B", weight=0.0):
        if mode == "B":
            l = [i for i in range(len(self.basic_containers)) if self.basic_containers[i] is None]
            if len(l) != 0:
                self.basic_containers[l[0]] = (CreateContainer.create_container(mode, weight))
            else:
                print("There is maximum amount of basic containers in this port")
        elif mode == "H":
            l=[i for i in range(len(self.heavy_containers)) if self.heavy_containers[i] is None]
            if len(l) != 0:
                self.heavy_containers[l[0]] = (CreateContainer.create_container(mode, weight))
            else:
                print("There is maximum amount of heavy containers in this port")
        elif mode == "R":
            l=[i for i in range(len(self.refrigirator_containers)) if self.refrigirator_containers[i] is None]
            if len(l) != 0:
                self.refrigirator_containers[l[0]] = (CreateContainer.create_container(mode, weight))
            else:
                print("There is maximum amount of basic refrigirated in this port")
        elif mode == "L":
            l=[i for i in range(len(self.liquid_containers)) if self.liquid_containers[i] is None]
            if len(l) != 0:
                self.liquid_containers[l[0]] = (CreateContainer.create_container(mode, weight))
            else:
                print("There is maximum amount of liquid containers in this port")

    def get_container(self, container):
        if isinstance(container, Container.BasicContainer):
            self.create_container("B", container.weight)
        if container is Container.HevyContainer:
            self.create_container("H", container.weight)
        if container is Container.RefrigiratorContainer:
            self.create_container("R", container.weight)
        if container is Container.LiquidContainer:
            self.create_container("L", container.weight)

    def give_container(self, container):
        if container in self.basic_containers or self.liquid_containers or self.heavy_containers or self.refrigirator_containers:
            if isinstance(container, Container.BasicContainer):
                print(self.basic_containers)
                self.basic_containers.remove(container)
                print(self.basic_containers)
                self.basic_containers.append(None)
                return True
            elif isinstance(container, Container.HevyContainer):
                self.heavy_containers.remove(container)
                self.basic_containers.append(None)
                return True
            elif isinstance(container, Container.RefrigiratorContainer):
                self.refrigirator_containers.remove(container)
                self.basic_containers.append(None)
                return True
            elif isinstance(container, Container.LiquidContainer):
                self.liquid_containers.remove(container)
                self.basic_containers.append(None)
                return True
        else:
            print("There is no such container in this port")
            return False
