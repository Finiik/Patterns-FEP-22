from typing import List
from piece import ChessPiece
from move_rule import MoveRule


class RookRule(MoveRule):
    def get_all_moves(self) -> List:
        x, y = self.position
        possible_moves = [[(x + i, y) for i in range(-7, 8) if 1 <= x + i <= 8],
                          [(x, y + i) for i in range(-7, 8) if 1 <= y + i <= 8]]
        return [move for direction in possible_moves for move in direction]


class Rook(ChessPiece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = RookRule(position)
