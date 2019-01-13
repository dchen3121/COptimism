from chess import *
import check_valid_moves


class Game:
    whiteCastleLeft = True
    whiteCastleRight = True
    BlackCastleLeft = True
    WhiteCastleRight = True

    def __init__(self):
        self.board = Board.initial_board()
        self.turn_number = 0

    def current_player_color(self):
        if self.turn_number % 2 == 0:
            return Color.WHITE
        else:
            return Color.BLACK

    def make_move(self, x1, y1, x2, y2):
        if (x2, y2) in check_valid_moves.valid_moves(x1, y1, self.board) and \
                self.board.get(x1, y1).color == self.current_player_color():
            self.board.move_piece(x1, y1, x2, y2)
            self.turn_number += 1
        else:
            print("invalid move, try again")


# game = Game()
# while True:
#     current_player_color = game.current_player_color()
#     print("current player: " + current_player_color.name)
#     print(game.board)
#     x1, y1 = map(int, input("enter your move start : x1, y1").split())
#     x2, y2 = map(int, input("enter your move end   : x2, y2").split())
#     game.make_move(x1, y1, x2, y2)
#     print("\n\n")


