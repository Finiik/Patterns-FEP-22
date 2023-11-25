from abc import ABC
from typing import List


def check_range(new_position: List[int]):
    for coordinate in new_position:
        if not 0 <= coordinate <= 8:
            raise ValueError("Invalid move")


class ChessPiece(ABC):
    def __init__(self, position: List[int], color: str):
        self.position = position
        self.color = color
        self.num_of_moves = 0
        self.move_rule = None

    def move(self, new_position: List[int]):
        check_range(new_position)
        self.position = new_position
        self.num_of_moves += 1
        return self.move_rule.get_all_moves()

    def print_info(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (f"Piece at {self.position}\n"
                f"Color: {self.color}\n"
                f"Moves: {self.num_of_moves}")
