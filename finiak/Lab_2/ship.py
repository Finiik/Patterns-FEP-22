from __future__ import annotations #пов'язує класи
from abc import ABC, abstractmethod #для абстрактних класів та методів
from dataclasses import dataclass #це щоб створити датаклас ConfigShip 
#Це робиться для того, аби робити клас ShipClass на два класи, один з яких націлений чисто на дані, а інший вже на функціонал
from typing import TYPE_CHECKING # запобігти нескінченному іморту класів

if TYPE_CHECKING:
    from containers import *
    from port import *

@dataclass
class ConfigShip:
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float   
    
class IShip(ABC):
    @abstractmethod
    def sailTo(self, port) -> bool:
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
    def __init__(self, id, Port: Port, shipConfig: ConfigShip, Containers: IContainer, fuel: float = 0.0) -> None:
        self.id = id
        self.fuel = fuel
        self.port = Port
        self.configs = shipConfig
        self._containersOnShip = Containers
        self._containersOnShipID = []
        self.usedContainers = []
        self.unloadedContainersID = []
        self._usedPortsID = []
        
    def __str__(self) -> str:
        return f"id: {self.id}\nFuel: {self.fuel}\nPort: {self.port}\nConfigs:\n\t{self.configs}\nContainers: {self.containersOnShip}"
    
    @property
    def containersOnShip(self):
        return self._containersOnShip
    
    @property
    def containersOnShipID(self):
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
    def usedPortsID(self):
        return self._usedPortsID
    
    def getExtraFuel(self) -> float:
        extraFuel = 0
        for shipContainer in self.containersOnShip:
            if type(shipContainer) != str:
                extraFuel += shipContainer.consumption()
            elif type(shipContainer) == str:
                continue
            return extraFuel
        
    def sailTo(self, port) -> bool:
        for currentPort in self.port:
            if (int(port.getDistance(currentPort))/self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer()) < self.fuel and currentPort.id not in self.usedPortsID:
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"Ship {self.id} has been sent to port {port.id}")
                return 1
            elif currentPort.id in self.usedPortsID:
                continue
            else:
                self.refuel(int(port.getDistance(currentPort))/self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer() - self.fuel)
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"Ship {self.id} has been refueled and sent to port {port.id}")
                return 1
            
    def refuel(self, amountOfFuelToAdd: float) -> None:
        if amountOfFuelToAdd < 0:
            raise ValueError(f"Amount of fuel given is less than 0")
        print(f"{amountOfFuelToAdd} litres has been added to previous amount of fuel: {self.fuel}")
        self.fuel += amountOfFuelToAdd
        
    def checkCompability(self, i: int) -> bool:
        if self.containersOnShip[i].weight <= self.configs.totalWeightCapacity:
            return 1
        else:
            return 0
        
    def deleteContainer(self, containerID) -> None:
        containers = [container for container in self.containersOnShip if container.id != containerID]
        self.containersOnShip = containers
        
    def load(self, containerID: uuid4) -> None:
        print("Container is loading on ship")
        currentContainerOnShip = self.containersOnShip
        for i in range(len(currentContainerOnShip)):
            for currentPort in self.port:
                if type(currentContainerOnShip[i]==str):
                    break
                elif containerID == currentContainerOnShip[i].id and self.checkCompability(i):
                    currentContainerOnShip.append(containerID)
                    currentPort.deleteContainer(containerID)
                    print(f"Container {containerID} has been loaded")
                    self.usedContainers.append(containerID)
                    if i > (len(self.usedContainers)-1) and containerID == self.usedContainers[i-1]:
                        break
                
    def unload(self, containerID):
        for shipContainer in self.containersOnShip:
            for currentPort in self.port:
                if type(shipContainer) == str:
                    break
                elif containerID in self.containersOnShipID and containerID not in self.unloadedContainersID:
                    self.containersOnShip.remove(shipContainer)
                    currentPort.currentContainersInPort.append(shipContainer)
                    self.unloadedContainersID.append(containerID)
                    print(f"Container {containerID} has been unloaded")
                elif containerID in self.unloadedContainersID:
                    continue
                else:
                    return ValueError(f"Container with ID {containerID} wasn't found")