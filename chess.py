from enum import Enum


class Piece:
    def __init__(self, type, color):
        # piece has two attributes: type and color
        self.type = type
        self.color = color

    def __str__(self):
        # returns the piece in string form, e.g. (wB) for white bishop
        if self.type == Type.KNIGHT:
            return "(" + self.color.name[0].lower() + "N" + ")"
        else:
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
        # initially it will be 64 squares all filled with "None"

    def __str__(self):
        # the tostring method prints out the 8 by 8 board in an 8 by 8 fashion
        board_str = ""
        for row in self.board:
            for piece in row:
                board_str += str(piece) + " "
            board_str += "\n"
        return board_str

    @staticmethod
    def is_in_range(x, y):
        """Returns true if x and y are both in the range [0, 7]. False otherwise"""
        return 0 <= x <= 7 and 0 <= y <= 7

    def get(self, x, y):
        """Return the Piece at index row x and column y"""
        return self.board[y][x]

    def set(self, x, y, piece):
        """Set the board at index row x and column y to piece"""
        self.board[y][x] = piece


'''
b = Board()
print(b)
print(Piece(Type.PAWN, Color.WHITE))
'''


