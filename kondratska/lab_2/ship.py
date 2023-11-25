from __future__ import annotations
from uuid import uuid4
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from container import Container
    from port import Port


@dataclass
class ConfigShip:
    """Dataclass containing Configuration of a Ship"""
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float


class IShip(ABC):
    """Interface of a Ship with abstract methods."""

    @abstractmethod
    def sail_to(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amountOfFuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass


class Ship(IShip):
    """Ship implementation"""

    def __init__(self, id, port: Port, shipConfig: ConfigShip, Containers: Container, fuel: float = 0.0) -> None:
        self.id = id
        self.fuel = fuel
        self.port = port
        self.configs = shipConfig
        self.containersOnShip = Containers
        self._containersOnShipID = []
        self.usedContainers = []
        self.unloadedContainersID = []
        self._used_portsID = []

    def __str__(self) -> str:
        return (f"id: {self.id}\nfuel: {self.fuel}\nport: {self.port}\n"
                f"configs:\n\t{self.configs}\ncontainers: {self.containersOnShip}")

    @property
    def containers_on_ship(self):
        return self.containersOnShip

    @property
    def containers_on_ship_ID(self):
        shipContainersID = []
        for shipContainer in self.containersOnShip:
            if type(shipContainer) == str:
                shipContainersID.append(shipContainer)
                continue
            else:
                shipContainersID.append(shipContainer.id)
        self._containersOnShipID = shipContainersID
        return self._containersOnShipID

    @property
    def used_portsID(self):
        return self._used_portsID

    def getExtraFuelConsumptionFromContainer(self) -> float:
        extraFuel = 0
        for shipContainer in self.containersOnShip:
            if type(shipContainer) != str:
                extraFuel += shipContainer.consumption()
            elif type(shipContainer) == str:
                continue
        return extraFuel

    def sail_to(self, port: Port) -> bool:
        for currentPort in self.port:
            if (int(port.get_distance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer()) < self.fuel and currentPort.id not in self.used_portsID:
                currentPort.incoming_ship(self)
                self._used_portsID.append(currentPort.id)
                print(f"Ship {self.id} was sent to {port.id} successfully.")
                continue
            elif currentPort.id in self.used_portsID:
                continue
            else:
                self.refuel(int(port.get_distance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer() - self.fuel)
                currentPort.incoming_ship(self)
                self.used_portsID.append(currentPort.id)
                print(f"Ship {self.id} now has {self.fuel} and has been successfully sent to port {port.id}")
                return True

    def refuel(self, amountOfFuelToAdd: float) -> None:
        if amountOfFuelToAdd < 0:
            raise ValueError(f"Amount of fuel given is less than 0.")
        print(f"{amountOfFuelToAdd} liters has been added to previous amount of fuel: {self.fuel}.")
        self.fuel += amountOfFuelToAdd

    def checkCompatibilityOfShipAndContainer(self, i: int) -> bool:
        if self.containersOnShip[i].weight <= self.configs.totalWeightCapacity:
            return True
        else:
            return False

    def deleteContainerOnShip(self, containerID) -> None:
        containers = [container for container in self.containersOnShip if container.id != containerID]
        self.containersOnShip = containers

    def load(self, containerID: uuid4) -> None:
        print("Loading container...")
        currentContainersOnShip = self.containersOnShip
        for i in range(len(currentContainersOnShip)):
            for currentPort in self.port:
                if type(currentContainersOnShip[i]) == str:
                    break
                elif containerID == currentContainersOnShip[i].id and self.checkCompatibilityOfShipAndContainer(i):
                    currentContainersOnShip.append(containerID)
                    currentPort.deleteContainer(containerID)
                    print(f"Container {containerID} has been successfully loaded.")
                    self.usedContainers.append(containerID)
                    if i > (len(self.usedContainers) - 1) and containerID == self.usedContainers[i - 1]:
                        break

    def unload(self, containerID):
        for shipContainer in self.containersOnShip:
            for currentPort in self.port:
                if type(shipContainer) == str:
                    break
                elif containerID in self._containersOnShipID and containerID not in self.unloadedContainersID:
                    self.containersOnShip.remove(shipContainer)
                    currentPort.currentContainersInPort.append(shipContainer)
                    self.unloadedContainersID.append(containerID)
                    print(f"Container {containerID} has been successfully unloaded.")
                elif containerID in self.unloadedContainersID:
                    continue
                else:
                    return ValueError(f"Container with ID {containerID} not found.")