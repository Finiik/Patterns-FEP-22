from abc import ABC, abstractmethod
from uuid import uuid4


class Container(ABC):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight
        self.items = []

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__(self, other) -> bool:
        id_check = self.id == other.id
        weight_check = self.weight == other.weight
        type_check = self.__class__ == other.__class__
        if id_check and weight_check and type_check:
            return True
        else:
            return False


class BasicContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def __repr__(self):
        return f"Basic cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def __repr__(self):
        return f"Heavy cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def __repr__(self):
        return f"Refrigerated cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def __repr__(self):
        return f"Liquid cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 4.0