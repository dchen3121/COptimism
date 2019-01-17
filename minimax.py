import eval_board_state
from chess import *
import check_valid_moves


def get_best_move(board, depth, color):
    """Return x1, x2 y1, y2, the coordinates of the initial position of the move and the final
    position of the move"""
    all_boards = all_valid_boards(board, color)
    # for board in all_boards:
    #     print(board)
    #     print(minimax(board, depth, color, False))
    # print("------------------------------------")
    best_board = None
    if color == Color.WHITE:
        best_board = max(all_valid_boards(board, color), key=lambda board: minimax(board, depth, color, True))
        print(best_board)
    else:
        best_board = min(all_valid_boards(board, color), key=lambda board: minimax(board, depth, color, False))
        print(best_board)
    x1, y1, x2, y2 = None, None, None, None
    return extract_move(board, best_board)

def extract_move(initial_board, final_board):
    x1, y1, x2, y2 = None, None, None, None
    for x in range(8):
        for y in range(8):
            if initial_board.get(x, y) is not None and final_board.get(x, y) is None:
                x1, y1 = x, y
            elif initial_board.get(x, y) is not None and final_board.get(x, y) is not None and \
                    initial_board.get(x, y) != final_board.get(x, y):
                x2, y2 = x, y
            elif initial_board.get(x, y) is None and final_board.get(x, y) is not None:
                x2, y2 = x, y
    # print(initial_board)
    # print(final_board)
    return x1, y1, x2, y2


def minimax(board, depth, color, is_max_player):
    """Minimax algorithm. Uses white as the reference color"""
    if depth == 0 or is_game_over(board, color):
        return eval_board_state.eval_board_state(board)
    if is_max_player:
        best_value = -100000000
        for child in all_valid_boards(board, color):
            best_value = max(best_value, minimax(child, depth - 1, color.other(), not is_max_player))
        return best_value
    else:
        best_value = 100000000
        for child in all_valid_boards(board, color):
            best_value = min(best_value, minimax(child, depth - 1, color.other(), not is_max_player))
        return best_value


def is_game_over(board, color):
    return check_valid_moves.is_in_check(board, color) and \
           len(check_valid_moves.moves_while_in_check(board, color)) == 0


def all_valid_boards(board, color):
    all_valid_boards = []
    if not check_valid_moves.is_in_check(board, color):
        for x in range(8):
            for y in range(8):
                if board.get(x, y) is not None and board.get(x, y).color == color:
                    for move in check_valid_moves.valid_moves(x, y, board):
                        child = board.copy()
                        child.move_piece(x, y, *move)
                        if not check_valid_moves.is_in_check(child, color):
                            all_valid_boards.append(child)
    else:
        all_valid_boards.append(check_valid_moves.boards_while_in_check(board, color))
    return all_valid_boards
'''
board = eval_board_state.sample_board_4
print(board)
for b in all_valid_boards(board, Color.WHITE):
    print(b)
    print(minimax(b, 0, Color.BLACK, False))
'''


