from typing import List
from piece import ChessPiece
from move_rule import MoveRule


class KnightRule(MoveRule):
    def get_all_moves(self) -> List:
        x, y = self.position
        possible_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]
        return [move for move in possible_moves if all(1 <= coord <= 8 for coord in move)]


class Knight(ChessPiece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = KnightRule(position)
