from __future__ import annotations #пов'язує класи
from abc import ABC, abstractmethod #для абстрактних класів та методів
from uuid import uuid4 #рандомайзер айдішок

class IContainer(ABC):
    def __init__(self, weight: float) -> None:
        self.weight = weight

    @abstractmethod #для того, щоб інші класи могли реалізовувати цей метод
    def __str__(self) -> str:
        pass #інтерфейс не має реалізації метода
    
    @abstractmethod
    def consumption(self) -> float:
        pass
    
    def __eq__(self, other) -> bool:
        idCheck = self.id == other
        if idCheck:
            return 1
        else:
            return 0
        
class BasicContainer(IContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)
        self.id = str(uuid4())
        
    def __str__(self) -> str:
        return f"Type: Basic Container\nWeight: {self.weight}\nID: {self.id}"
    
    def consumption(self) -> float:
        return self.weight * 2.5
    
    
class HeavyContainer(IContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight = weight)
        self.id = str(uuid4())
        
    def __str__(self) -> str:
        return f"Type: Heavy Container:\nWeight: {self.weight}\nID: {self.id}"
    
    def consumption(self) -> float:
        return self.weight * 3.0
    

class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight = weight)
        self.id = str(uuid4())
        
    def __str__(self) -> str:
        return f"Type: Refrigerated Container:\nWeight: {self.weight}\nID: {self.id}"
    
    def consumption(self) -> float:
        return self.weight * 5.0
    

class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight = weight)
        self.id = str(uuid4())
        
    def __str__(self) -> str:
        return f"Type: Liquid Container:\nWeight: {self.weight}\nID: {self.id}"
    
    def consumption(self) -> float:
        return self.weight * 4.0