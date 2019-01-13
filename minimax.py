import eval_board_state
from chess import *
import check_valid_moves

def minimax(board, depth, color, is_max_player):
    """Minimax algorithm. Uses white as the reference color"""
    if depth == 0 or is_game_over(board):
        return eval_board_state.eval_board_state(board)
    if is_max_player:
        best_value = -100000000
        for child in all_valid_boards(board, color):
            best_value = max(best_value, minimax(board, depth - 1, color.other(), not is_max_player))
        return best_value
    else:
        best_value = 100000000
        for child in all_valid_boards(board, color):
            best_value = min(best_value, minimax(board, depth - 1, color.other(), not is_max_player))
        return best_value




def is_game_over(board):
    return len(check_valid_moves.moves_while_in_check(board)) == 0

def all_valid_boards(board, color):
    all_valid_boards = []
    is_in_check = check_valid_moves.is_in_check(board, color)
    if is_in_check == False or is_in_check.color == color.other():
        for x in range(8):
            for y in range(8):
                for move in check_valid_moves.valid_moves(x, y, board):
                    all_valid_boards.append(board.copy().move_piece(x, y, *move))
    else:
        all_valid_boards.append(check_valid_moves.boards_while_in_check(board))
    return all_valid_boards

board = Board.initial_board()
for board in all_valid_boards(board, Color.WHITE):
    print(board)




