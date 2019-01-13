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

sample_board_1 = Board(
    [[wR, wN, wB, wQ, wK, wB, wN, wR],
     [wP, wP, wP, wP, wP, wP, wP, wP],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [bP, bP, bP, bP, bP, bP, bP, bP],
     [bR, bN, bB, bQ, bK, bB, bN, bR],]
)
sample_board_2 = Board(
    [[bR, bN, bB, bQ, bK, bB, bN, bR],
     [bP, bP, bP, None, bP, bP, bP, bP],
     [None, None, None, None, None, None, None, None],
     [None, None, None, bP, None, None, None, None],
     [None, None, None, wP, None, None, None, None],
     [None, None, wN, None, None, None, None, None],
     [wP, wP, wP, None, wP, wP, wP, wP],
     [wR, None, wB, None, wK, wB, wN, wR]]
)


# check_material_value(board_input) returns a list of length 2 in form [int, int]
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
def controls_centre(piece_input, x, y):
    white_val = 0
    black_val = 0
    if piece_input is not None:
        if piece_input.color == Color.WHITE:
            if piece_input.type == Type.PAWN:
                if (x == 2 and y == 2) or (x == 5 and y == 2) or (x == 2 and y == 3) or (x == 5 and y == 3) or (x == 3 and y == 2) or (x == 4 and y == 2):
                    white_val += 0.2
                elif (x == 3 and y == 3) or (x == 4 and y == 3):
                    white_val += 0.4
                elif (x == 3 and y == 4) or (x == 4 and y == 4):
                    white_val += 0.3
                else:
                    white_val += 0
            if piece_input.type == Type.KNIGHT:
                if (x, y) in [(1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (6, 3),
                              (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4)]:
                    white_val += 0.2
                if (x, y) in [(2, 2), (5, 2), (2, 5), (5, 5)]:
                    white_val += 0.4
                if (x, y) in [(3, 3), (4, 3), (3, 4), (4, 4), (2, 3), (2, 4), (3, 2), (4, 2), (5, 3), (5, 4), (3, 5), (3, 6)]:
                    white_val += 0.3
            if piece_input.type == Type.BISHOP:
                if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                              (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                    white_val += 0.2
            if piece_input.type == Type.ROOK:
                if x in [3, 4]:
                    white_val += 0.1
                if y in [3, 4]:
                    white_val += 0.1
            if piece_input.type == Type.QUEEN:
                if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                              (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                    white_val += 0.1
                if x in [3, 4]:
                    white_val += 0.1
                if y in [3, 4]:
                    white_val += 0.1
        elif piece_input.color == Color.BLACK:
            if piece_input.type == Type.PAWN:
                if (x == 2 and y == 5) or (x == 5 and y == 5) or (x == 2 and y == 4) or (x == 5 and y == 4) or (x == 3 and y == 5) or (x == 4 and y == 5):
                    black_val += 0.2
                elif (x == 3 and y == 4) or (x == 4 and y == 4):
                    black_val += 0.4
                elif (x == 3 and y == 3) or (x == 4 and y == 3):
                    black_val += 0.3
                else:
                    black_val += 0
            if piece_input.type == Type.KNIGHT:
                if (x, y) in [(1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (6, 3),
                              (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4)]:
                    black_val += 0.2
                if (x, y) in [(2, 2), (5, 2), (2, 5), (5, 5)]:
                    black_val += 0.4
                if (x, y) in [(3, 3), (4, 3), (3, 4), (4, 4), (2, 3), (2, 4), (3, 2), (4, 2), (5, 3), (5, 4), (3, 5), (3, 6)]:
                    black_val += 0.3
            if piece_input.type == Type.BISHOP:
                if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                              (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                    black_val += 0.2
            if piece_input.type == Type.ROOK:
                if x in [3, 4]:
                    black_val += 0.1
                if y in [3, 4]:
                    black_val += 0.1
            if piece_input.type == Type.QUEEN:
                if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                              (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                    black_val += 0.1
                if x in [3, 4]:
                    black_val += 0.1
                if y in [3, 4]:
                    black_val += 0.1
    return [white_val, black_val]
# check_centre_points(board_input) returns a list of length 2 in form [num, num]
# the first num is the total material of white's pieces
# the second num is the total material of black's pieces
def check_centre_points(board_input):
    white_centre = 0
    black_centre = 0
    for x in range(0, 8):
        for y in range(0, 8):
            points_list = controls_centre(board_input.get(x, y), x, y)
            white_centre += points_list[0]
            black_centre += points_list[1]
    return [white_centre, black_centre]




# print(check_material_value(sample_board_1))
# print(check_centre_points(sample_board_1))
#
# print(check_material_value(sample_board_2))
# print(check_centre_points(sample_board_2))
