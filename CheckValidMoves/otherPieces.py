# Valid moves for rook, and knight

from chess import*

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


def valid_move_knight(x, y, board, color):
    moves_knight = []
    counters_list = [[3, 2], [3, -2], [-3, 2], [-3, -2], [2, 3], [-2, 3], [2, -3], [-2, -3]]
    index = 0

    while index <= len(counters_list) - 1:
        if in_bound(x + counters_list[index][0], y + counters_list[index][1]) and \
                (board.get(x + counters_list[index][0], y + counters_list[index][1]) is None or
                board.get(x + counters_list[index][0], y + counters_list[index][1]) != color):
            moves_knight += [(x + counters_list[index][0], y + counters_list[index][1])]
        index += 1

    return moves_knight


b = Board()
b.set(2, 3, Piece(Type.ROOK, Color.BLACK))
b.set(4, 4, Piece(Type.KNIGHT, Color.WHITE))



print(b)

print(valid_move_rook (2, 3, b, Color.BLACK))
print(valid_move_knight (5, 6, b, Color.BLACK))

