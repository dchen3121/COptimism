from chess import*

def valid_move (x, y, board):

    piece = board[x][y]
    type = piece.type
    color = piece.color

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

b = Board()
b.set(2, 3, Piece(Type.BISHOP, Color.BLACK))
b.set(5, 6, Piece(Type.BISHOP, Color.BLACK))
b.set(1, 2, Piece(Type.BISHOP, Color.WHITE))


print(b)

print (valid_move_bishop(2, 3, b, Color.BLACK))















