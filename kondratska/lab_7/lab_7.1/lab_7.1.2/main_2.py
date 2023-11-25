from piece import ChessPiece
from knight import Knight
from rook import Rook
from bishop import Bishop
from king import King
from typing import List


def test_piece_movement(piece: ChessPiece, new_position: List[int]):
    print(f"\nTesting {type(piece).__name__} movement:")
    print("Initial state:")
    print(piece)

    try:
        moves = piece.move(new_position)
        print(f"Moved to {new_position}")
        print(f"Available moves: {moves}")
        print(piece)
    except ValueError as e:
        print(f"Error: {e}")


"""testing the knight"""
knight = Knight([1, 2], 'White')
test_piece_movement(knight, [3, 4])

"""testing the bishop"""
bishop = Bishop([3, 3], 'Black')
test_piece_movement(bishop, [5, 5])

"""testing the rook"""
rook = Rook([4, 4], 'White')
test_piece_movement(rook, [4, 8])

"""testing the king"""
king = King([1, 4], 'White')
test_piece_movement(rook, [2, 4])
