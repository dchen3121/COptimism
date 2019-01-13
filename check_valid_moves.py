from chess import*

def is_in_check(board):

    whiteKing = board.search(Type.KING, Color.WHITE)
    blackKing = board.search(Type.KING, Color.BLACK)

    blackPieceMoves = []
    whitePieceMoves = []


    for x in range(0, 8):
        for y in range(0, 8):
            piece = board.get(x, y)
            if piece is not None and piece.color == Color.BLACK and piece.type != Type.KING:
                blackPieceMoves += valid_moves(piece)

            if piece is not None and piece.color == Color.WHITE and piece.type != Type.KING:
                whitePieceMoves += valid_moves(piece)

    blackPieceMoves = list(set(blackPieceMoves))
    whitePieceMoves = list(set(whitePieceMoves))

    if whiteKing in blackPieceMoves:
        return True

    if blackKing in whitePieceMoves:
        return True

    return False

def moves_while_in_check(board):
    moves = []
    for x in range(0, 8):
        for y in range(0, 8):
            if board.get(x, y) is not None:
                for move in valid_moves(x, y, board):
                    b = board.copy
                    if not is_in_check(b.move(x, y, move[0], move[1])):
                        moves += [move]

    return moves



####################################################################
def valid_moves(x, y, board):

    piece = board.get(x, y)
    type = piece.type
    color = piece.color

    if type == Type.BISHOP:
        return valid_move_bishop(x, y, board, color)

    if type == Type.PAWN:
        return valid_move_pawn(x, y, board, color)

    if type == Type.KING:
        return valid_move_king(x, y, board, color)

    if type == Type.ROOK:
        return valid_move_rook(x, y, board, color)

    if type == Type.QUEEN:
        return valid_move_queen(x, y, board, color)

    if type == Type.KNIGHT:
        return valid_move_knight(x, y, board, color)
#################################################################################





def inBounds(x , y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True

    else:
        return False

def valid_move_bishop(x , y, board, color):

    posMoves = []

    counter = 1

    while inBounds(x + counter, y + counter):
        if board.get(x + counter , y + counter) is None or board.get(x + counter, y + counter).color != color:
            posMoves += [(x + counter, y + counter)]

        else:
            break

        counter += 1
    counter = 1

    while inBounds(x + counter, y - counter):
        if board.get(x + counter, y - counter) is None or board.get(x + counter, y - counter).color != color:
            posMoves += [(x + counter, y - counter)]

        else:
            break

        counter += 1



    counter = 1

    while inBounds(x - counter, y + counter):
        if board.get(x - counter, y + counter) is None or board.get(x - counter, y + counter).color != color:
            posMoves += [(x - counter, y + counter)]

        else:
            break
        counter += 1

    counter = 1

    while inBounds(x - counter, y - counter):
        if board.get(x - counter, y - counter) is None or board.get(x - counter, y - counter).color != color:
            posMoves += [(x - counter, y - counter)]

        else:
            break

        counter += 1

    return posMoves


def valid_move_pawn(x, y, board, color):
    posMoves = []

    if color == Color.WHITE:
        if inBounds(x, y + 1) and board.get(x, y + 1) is None:
            posMoves += [(x, y + 1)]

        if y == 1 and board.get(x, y + 2) is None:
            posMoves += [(x, y + 2)]

    else:
        if inBounds(x, y - 1) and board.get(x, y - 1) is None:
            posMoves += [(x, y - 1)]

        if y == 6 and board.get(x, y - 2) is None:
            posMoves += [(x, y - 2)]

    return posMoves


def valid_move_king(x , y, board, color):
    posMoves = []

    if inBounds(x, y + 1) and (board.get(x, y + 1) is None or board.get(x, y + 1).color != color):
        posMoves += [(x, y + 1)]

    if inBounds(x + 1, y + 1) and (board.get(x + 1, y + 1) is None or board.get(x + 1, y + 1).color != color):
        posMoves += [(x + 1, y + 1)]

    if inBounds(x + 1, y) and (board.get(x + 1, y) is None or board.get(x + 1, y).color != color):
        posMoves += [(x + 1, y)]

    if inBounds(x + 1, y - 1) and (board.get(x + 1, y - 1) is None or board.get(x + 1, y - 1).color != color):
        posMoves += [(x + 1, y - 1)]

    if inBounds(x, y - 1) and (board.get(x, y - 1) is None or board.get(x, y - 1).color != color):
        posMoves += [(x, y - 1)]

    if inBounds(x - 1, y - 1) and (board.get(x - 1, y - 1) is None or board.get(x - 1, y - 1).color != color):
        posMoves += [(x - 1, y - 1)]

    if inBounds(x - 1, y) and (board.get(x - 1, y) is None or board.get(x - 1, y).color != color):
        posMoves += [(x - 1, y)]

    if inBounds(x - 1, y + 1) and (board.get(x - 1, y + 1) is None or board.get(x - 1, y + 1).color != color):
        posMoves += [(x - 1, y + 1)]

    return posMoves


def valid_move_queen(x, y, board, color):
    return valid_move_bishop(x , y, board, color) + valid_move_rook(x, y, board, color)







#
# b = Board()
# b.set(2, 3, Piece(Type.BISHOP, Color.BLACK))
# b.set(5, 6, Piece(Type.KING, Color.BLACK))
# b.set(1, 2, Piece(Type.BISHOP, Color.WHITE))
# b.set(5, 7, Piece(Type.QUEEN, Color.BLACK))
# b.set(4, 4, Piece(Type.ROOK, Color.BLACK))
#
# print(b)
#
# print(valid_move_bishop(2, 3, b, Color.BLACK))
# print(valid_moves(2, 3, b))
# print(valid_move_king(5, 6, b, Color.BLACK))
# print(valid_move_bishop(5, 7, b, Color.BLACK))


def in_bound(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False


def valid_move_rook(x, y, board, color):
    moves_rook = []

    counter = 1

    while in_bound(x + counter, y):
        if board.get(x + counter, y) is None or board.get(x + counter, y).color != color:
            moves_rook += [(x + counter, y)]
        else:
            break
        counter += 1

    counter = 1

    while in_bound(x - counter, y):
        if board.get(x - counter, y) is None or board.get(x - counter, y).color != color:
            moves_rook += [(x - counter, y)]
        else:
            break
        counter -= 1

    counter = 1

    while in_bound(x, y + counter):
        if board.get(x, y + counter) is None or board.get(x,y + counter).color != color:
            moves_rook += [(x, y + counter)]
        else:
            break
        counter += 1

    counter = 1

    while in_bound(x, y - counter):
        if board.get(x, y - counter) is None or board.get(x, y - counter).color != color:
            moves_rook += [(x, y - counter)]
        else:
            break
        counter += 1

    return moves_rook


def valid_move_knight(x, y, board, color):
    moves_knight = []
    counters_list = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
    index = 0

    while index <= len(counters_list) - 1:
        if in_bound(x + counters_list[index][0], y + counters_list[index][1]) and \
                (board.get(x + counters_list[index][0], y + counters_list[index][1]) is None or
                board.get(x + counters_list[index][0], y + counters_list[index][1]) != color):
            moves_knight += [(x + counters_list[index][0], y + counters_list[index][1])]
        index += 1

    return moves_knight



#
#
# print(valid_move_rook(4, 4, b, Color.BLACK))




