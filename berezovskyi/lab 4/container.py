from dataclasses import dataclass


@dataclass
class ContainerDetails:
    ID: str
    weight: int


class IContainer:
    def consumption(self) -> int:
        pass


class Container(IContainer):
    def __init__(self, ID: str, weight: int):
        self.id = ID
        self.weight = weight

    def consumption(self) -> int:
        return self.weight // 10


def get_type():
    return None
