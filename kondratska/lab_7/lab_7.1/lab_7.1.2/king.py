from typing import List
from piece import ChessPiece
from move_rule import MoveRule


class KingRule(MoveRule):
    def get_all_moves(self) -> List:
        x, y = self.position
        possible_moves = [
            (x + 1, y), (x, y + 1),
            (x - 1, y), (x, y - 1),
            (x + 1, y + 1), (x - 1, y - 1),
            (x - 1, y + 1), (x + 1, y - 1)
        ]
        return [move for move in possible_moves if all(1 <= coord <= 8 for coord in move)]


class King(ChessPiece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = KingRule(position)
