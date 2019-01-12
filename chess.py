from enum import Enum

class Piece:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def __str__(self):
        return "(" + self.color.name[0].lower() + self.type.name[0] + ")"

class Type(Enum):
    PAWN = 1
    BISHOP = 2
    KNIGHT = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Color(Enum):
    WHITE = 0
    BLACK = 1


class Board:
    def __init__(self):
        # board is a 2D list of pieces, 8 by 8
        self.board = [[None for x in range(8)] for y in range(8)]
        self.board[1][1] = Piece(Type.PAWN, Color.WHITE)

    def __str__(self):
        board_str = ""
        for row in self.board:
            for piece in row:
                board_str += str(piece) + " "
            board_str += "\n"
        return board_str



b = Board()
print(b)
print(Piece(Type.PAWN, Color.WHITE))



