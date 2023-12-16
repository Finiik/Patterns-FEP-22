from abc import ABC
from typing import List


class MoveRule(ABC):
    def __init__(self, position: List[int]):
        self.position = position

    def get_all_moves(self) -> List:
        pass
