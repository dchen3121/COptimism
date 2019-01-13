# Valid moves for bishop, rook, and knight


def in_bound(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False


def valid_moves_rook(x, y, board, color):
    moves_rook = []

    counter = 1

    while in_bound(x + counter, y):
        if board.get(x + counter, y) is None or board.get(x + counter, y).color != color:
            moves_rook += [(x + counter, y)]
        counter += 1

    counter = 1

    while in_bound(x - counter, y):
        if board.get(x - counter, y) is None or board.get(x - counter, y).color != color:
            moves_rook += [(x - counter, y)]
        counter -= 1

    counter = 1

    while in_bound(x, y + counter):
        if board.get(x, y + counter) is None or board.get(x,y + counter).color != color:
            moves_rook += [(x, y + counter)]
        counter += 1

    counter = 1

    while in_bound(x, y - counter):
        if board.get(x, y - counter) is None or board.get(x, y - counter).color != color:
            moves_rook += [(x, y - counter)]
        counter += 1

    return moves_rook
