from chess import *

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

sample_board = Board(
    [[bR, bN, bB, bQ, bK, bB, bN, bR],
     [bP, bP, bP, bP, bP, bP, bP, bP],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [wP, wP, wP, wP, wP, wP, wP, wP],
     [wR, wN, wB, wQ, wK, wB, wN, wR]]
)

# check_material_value(board) returns a list of length 2 in form [int, int]
# the first int is the total material of white's pieces
# the second int is the total material of black's pieces
def check_material_value(board_input):
    white_mat = 0
    black_mat = 0
    for row in board_input.board:
        for piece in row:
            if piece is not None:
                if piece.color == Color.WHITE:
                    if piece.type == Type.PAWN:
                        white_mat += 1
                    elif piece.type == Type.KNIGHT or piece == Type.BISHOP:
                        white_mat += 3
                    elif piece.type == Type.ROOK:
                        white_mat += 5
                    elif piece.type == Type.QUEEN:
                        white_mat += 9
                    else:
                        white_mat += 0
                elif piece.color == Color.BLACK:
                    if piece.type == Type.PAWN:
                        black_mat += 1
                    elif piece.type == Type.KNIGHT or piece == Type.BISHOP:
                        black_mat += 3
                    elif piece.type == Type.ROOK:
                        black_mat += 5
                    elif piece.type == Type.QUEEN:
                        black_mat += 9
                    else:
                        black_mat += 0
    return [white_mat, black_mat]


# returns an num if a piece is in reach of the centre and 0 if it isn't
# return type is [whiteVal, blackVal]
def controls_centre(piece_input, board_input, x, y):
    white_val = 0
    if piece_input.color == Color.WHITE:
        if piece_input.type == Type.PAWN:
            if (x == 2 and y == 2) or (x == 5 and y == 2) or (x == 2 and y == 3) or (x == 5 and y == 3) or (x == 3 and y == 2) or (x == 4 and y == 2):
                white_val += 0.2
            elif (x == 3 and y == 3) or (x == 4 and y == 3):
                white_val += 0.4
            elif (x == 3 and y == 4) or (x == 4 and y == 4):
                white_val += 0.25
            else:
                white_val += 0
        if piece_input.type == Type.KNIGHT:
            if (x, y) in [(1, 3), (1, 4), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (6, 3)]:
                white_val += 0.2


    elif piece_input.color == Color.BLACK:
        return 0


def check_centre_points(board_input):
    white_centre = 0
    black_centre = 0
    for x in range(0, 8):
        for y in range(0, 8):
            return 0




print(check_material_value(sample_board))