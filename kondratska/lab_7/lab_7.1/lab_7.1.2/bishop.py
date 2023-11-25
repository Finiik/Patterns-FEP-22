from typing import List
from piece import ChessPiece
from move_rule import MoveRule


class BishopRule(MoveRule):
    def get_all_moves(self) -> List:
        x, y = self.position
        possible_moves = [[(x + i, y + i) for i in range(-7, 8) if 1 <= x + i <= 8 and 1 <= y + 1 <= 8],
                          [(x - i, y - i) for i in range(-7, 8) if 1 <= x - i <= 8 and 1 <= y - 1 <= 8]]
        return possible_moves


class Bishop(ChessPiece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = BishopRule(position)
