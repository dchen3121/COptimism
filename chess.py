from enum import Enum
from copy import deepcopy


class Piece:
    def __init__(self, type, color):
        # piece has two attributes: type and color
        self.type = type
        self.color = color

    def __str__(self):
        """Returns the string representation of a piece, e.g. (wB) for white bishop"""
        if self.type == Type.KNIGHT:
            return self.color.name[0].lower() + "N"
        else:
            return self.color.name[0].lower() + self.type.name[0]

    def __eq__(self, other):
        """Returns true if self and other are have equivalent type and color, or if they are both None.
        False otherwise"""
        if self is None and other is None:
            return True
        if self is not None and other is not None:
            return self.type == other.type and self.color == other.color
        else:
            return False

    def __hash__(self):
        return self.type.__hash__() + self.color.__hash__()


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

    def other(self):
        if self == Color.WHITE:
            return Color.BLACK
        else:
            return Color.WHITE


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
            self.board = deepcopy(board)

    @staticmethod
    def initial_board():
        """Create a new Board with Pieces placed like they should be at the beginning of a match"""
        wP = Piece(Type.PAWN, Color.WHITE)
        wN = Piece(Type.KNIGHT, Color.WHITE)
        wB = Piece(Type.BISHOP, Color.WHITE)
        wR = Piece(Type.ROOK, Color.WHITE)
        wQ = Piece(Type.QUEEN, Color.WHITE)
        wK = Piece(Type.KING, Color.WHITE)

        bP = Piece(Type.PAWN, Color.BLACK)
        bN = Piece(Type.KNIGHT, Color.BLACK)
        bB = Piece(Type.BISHOP, Color.BLACK)
        bR = Piece(Type.ROOK, Color.BLACK)
        bQ = Piece(Type.QUEEN, Color.BLACK)
        bK = Piece(Type.KING, Color.BLACK)

        return Board(
            [[wR, wN, wB, wQ, wK, wB, wN, wR],
             [wP, wP, wP, wP, wP, wP, wP, wP],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [bP, bP, bP, bP, bP, bP, bP, bP],
             [bR, bN, bB, bQ, bK, bB, bN, bR]]
        )

    def copy(self):
        """Return a new copy of the Board"""
        return Board(self.board)

    def __str__(self):
        """Return a pretty string representation of the 8x8 internal board.
        The (0,0) piece is printed at the bottom left corner."""
        board_str = "  "
        for x in range(8):
            board_str += "-" + str(x) + "-"
        board_str += "\n"
        for row_index, row in enumerate(reversed(self.board)):
            board_str += str(7 - row_index) + "| "
            for piece in row:
                if piece is None:
                    board_str += "   "
                else:
                    board_str += str(piece) + " "
            board_str += "|\n"
        return board_str + "  " + "---" * 8 + "\n"

    @staticmethod
    def is_in_range(x, y):
        """Return true if x and y are both in the range [0, 7]. False otherwise"""
        return 0 <= x <= 7 and 0 <= y <= 7

    def get(self, x, y):
        """Return the Piece at index row x and column y"""
        return self.board[y][x]

    def set(self, x, y, piece):
        """Set the board at index row x and column y to piece"""
        self.board[y][x] = piece

    def move_piece(self, x1, y1, x2, y2):
        """Move the piece at index (x1, y1) to the position at index (x2, y2),
        only if the (x1, y2) is not an empty piece (None). Otherwise, do nothing.
        NOTE: this modifies the board in-place."""
        old_piece = self.get(x1, y1)  # old piece to be moved
        if old_piece is not None:
            self.set(x2, y2, old_piece)
            self.set(x1, y1, None)  # the old position should now be an empty piece

    def search(self, piece):
        """Search the internal board and return a list of all the coordinate tuples (x, y)
        where the piece exists"""
        # TO DO: use a dict to map pieces to their locations: to speed up search
        found = []
        for row in range(8):
            for col in range(8):
                if self.get(col, row) == piece:
                    found.append((col, row))
        return found


# board = Board.initial_board()
# print(board)
# print(board.search(Piece(Type.KING, Color.WHITE)))

# board = Board.initial_board()
# print(board)
# a = board.copy()
# a.move_piece(0, 0, 3, 3)
# print(board)






