from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import uuid4


class Container(ABC):
  def __init__(self, weight: float) -> None:
    self.weight = weight

  @abstractmethod
  def __str__(self) -> str:
    pass

  @abstractmethod
  def consumption(self) -> float:
    pass

  def __eq__(self, other) -> bool:
    idСheck = self.id == other
    # weightСheck = self.weight == other.weight
    # typeСheck = self.__class__ == other.__class__
    if idСheck:
      return True
    else:
      return False


class BasicContainer(Container):
  def __init__(self, weight: float) -> None:
    super().__init__(weight=weight)
    self.id = str(uuid4())

  def __str__(self) -> str:
    return f"Type: Basic Container\nWeight: {self.weight}\nID: {self.id}"

  def consumption(self) -> float:
    return self.weight * 2.5


class HeavyContainer(Container):
  def __init__(self, weight: float) -> None:
    super().__init__(weight=weight)
    self.id = str(uuid4())
  
  def __str__(self) -> str:
    return f"Type: Heavy Container\nWeight: {self.weight}\nID: {self.id}"


  def consumption(self) -> float:
    return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
  def __init__(self, weight: float) -> None:
    super().__init__(weight=weight)
    self.id = str(uuid4())

  def __str__(self) -> str:
    return f"Type: Refrigerated Container\nWeight: {self.weight}\nID: {self.id}"

    
  def consumption(self) -> float:
    return self.weight * 5.0


class LiquidContainer(HeavyContainer):
  def __init__(self, weight: float) -> None:
    super().__init__(weight=weight)
    self.id = str(uuid4())


  def __str__(self) -> str:
    return f"Type: Liquid Container\nWeight: {self.weight}\nID: {self.id}"


  def consumption(self) -> float:
    return self.weight * 4.0
