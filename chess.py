from enum import Enum


class Piece:
    def __init__(self, type, color):
        # piece has two attributes: type and color
        self.type = type
        self.color = color

    def __str__(self):
        # returns the piece in string form, e.g. (wB) for white bishop
        if self.type == Type.KNIGHT:
            return self.color.name[0].lower() + "N"
        else:
            return self.color.name[0].lower() + self.type.name[0]


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
    """Create a new Board.
    If a board argument is not given, the internal board representation is set to None in all 64 positions.
    Otherwise, the internal board is set to the value of the argument board"""
    def __init__(self, board=None):
        # board is a 2D list of pieces, 8 by 8
        if board is None:
            # initially it will be 64 squares all filled with "None"
            self.board = [[None for x in range(8)] for y in range(8)]
        else:
            self.board = board

    def __str__(self):
        """Returns a pretty string representation of the 8x8 internal board."""
        board_str = " "
        for x in range(8):
            board_str += "-" + str(x) + "-"
        board_str += "\n"
        for row_index, row in enumerate(self.board):
            board_str += str(row_index)
            for piece in row:
                if piece is None:
                    board_str += "   "
                else:
                    board_str += str(piece) + " "
            board_str += "|\n"
        return board_str + " " + "---" * 8 + "\n"

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


# b = Board()
# b.set(1, 1, Piece(Type.KNIGHT, Color.WHITE))
# b.set(3, 0, Piece(Type.BISHOP, Color.BLACK))
# print(b)



