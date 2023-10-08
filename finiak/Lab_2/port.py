from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import uuid4
from ship import Ship
from containers import *
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


class IPort(ABC):
    
    @abstractmethod
    def incomingShip(self, ship: Ship):
        pass
    
    @abstractmethod
    def outgoingShip(self, ship: Ship):
        pass
    

class Port(IPort):
    def __init__(self, id: uuid4, latitude: float, longitude: float, howManyContainersInPort: IContainer = []) -> None:
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self._howManyContainersInPort = howManyContainersInPort
        self.shipHistory = []
        self.currentShips = []
    
    def __str__(self) -> str:
        return f"ID: {self.id}\nLatitude: {self.latitude}\nLongitude: {self.longitude}\nCurrent Ships: {self.currentShips}\nCurrent Containers: [{self.howManyContainersInPort}]"
    
    @property
    def howManyContainersInPort(self):
        return self._howManyContainersInPort
    
    @howManyContainersInPort.setter
    def howManyContainersInPort(self, value):
        self.howManyContainersInPort = value

    def deleteContainer(self, containerID) -> str:
        if not self.howManyContainersInPort:
            raise AttributeError(f"Container {containerID} hasn't been found.")
        for container in self.howManyContainersInPort:
            if type(container) != str:
                if container.id == containerID:
                    self.howManyContainersInPort.remove(container)
                    return f"Container {containerID} has been removed from port {self.id}"
                elif type(container) == str:
                    continue
                
    def getDistance(self, otherPort: Port) -> float:
        distance = haversine(self.latitude, self.longitude, otherPort.latitude, otherPort.longitude)
        return distance
    
    def incomingShip(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.currentShips:
            self.currentShips.append(ship)
            return 1
        else:
            print(f"Failed to add {ship.id} to current ship list.\nCurrent ships are: {self.currentShips}")
            return 0
        
    def outgoingShip(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship in self.currentShips:
            self.shipHistory.append(ship)
            print(f"Ship {ship.id} was added to port {self.id}")
            return 1
        else:
            print(f"Failed to load ship {ship.id} to port {self.id}")
            return 0