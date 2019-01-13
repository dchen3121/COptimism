from chess import*

def valid_moves (x, y, board):

    piece = board.get(x, y)
    type = piece.type
    color = piece.color

    if type == Type.BISHOP:
        return valid_move_bishop(x, y, board, color)

    if type == Type.PAWN:
        return valid_move_pawn(x, y, board, color)

    if type == Type.KING:
        return valid_move_king(x, y, board, color)



def inBounds(x , y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True

    else:
        return False

def valid_move_bishop(x , y, board, color):

    posMoves = []

    counter = 1

    while inBounds(x + counter , y + counter):
        if board.get(x + counter , y + counter) is None or board.get(x + counter, y + counter).color != color:
            posMoves += [(x + counter, y + counter)]
        counter += 1
    counter = 1

    while inBounds(x + counter, y - counter):
        if board.get(x + counter, y + counter) is None or board.get(x + counter, y + counter).color != color:
            posMoves += [(x + counter, y - counter)]
        counter += 1

    counter = 1

    while inBounds(x - counter, y + counter):
        if board.get(x + counter, y + counter) is None or board.get(x + counter, y + counter).color != color:
            posMoves += [(x - counter, y + counter)]
        counter += 1

    counter = 1

    while inBounds(x - counter, y - counter):
        if board.get(x + counter, y + counter) is None or board.get(x + counter, y + counter).color != color:
            posMoves += [(x - counter, y - counter)]
        counter += 1

    return posMoves


def valid_move_pawn(x , y, board, color):
    posMoves = []

    if inBounds(x + y + 1) and (board.get(x, y + 1) is None or board.get(x, y + 1).color != color):
        posMoves += [(x, y + 1)]

    if inBounds(x, y + 2) and (board.get(x, y + 2) is None or board.get(x, y + 2).color != color):
        posMoves += [(x, y + 2)]

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

#
# def valid_move_queen(x, y, board, color):
#     return valid_move_bishop(x , y, board, color) +
#
#






b = Board()
b.set(2, 3, Piece(Type.BISHOP, Color.BLACK))
b.set(5, 6, Piece(Type.KING, Color.BLACK))
b.set(1, 2, Piece(Type.BISHOP, Color.WHITE))



print(b)

print(valid_move_bishop(2, 3, b, Color.BLACK))
print(valid_moves(2, 3, b))
print(valid_move_king(5, 6, b, Color.BLACK))









