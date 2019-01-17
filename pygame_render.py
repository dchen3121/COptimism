import sys
import os

from game import Game
from chess import *
import pygame
import check_valid_moves
import minimax

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
width, height, = 560, 560
pwidth, pheight = 70, 70
BACK_COLOR = (255, 255, 255)
SELECT_COLOR = (110, 110, 200)
POSSIBLE_COLOR = (110, 110, 200)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# load images for the pieces
piece_to_image = {}
piece_to_image[Piece(Type.PAWN, Color.BLACK)] = pygame.image.load("images/bPawn.png")
piece_to_image[Piece(Type.BISHOP, Color.BLACK)] = pygame.image.load("images/bBishop.png")
piece_to_image[Piece(Type.KNIGHT, Color.BLACK)] = pygame.image.load("images/bKnight.png")
piece_to_image[Piece(Type.ROOK, Color.BLACK)] = pygame.image.load("images/bRook.png")
piece_to_image[Piece(Type.QUEEN, Color.BLACK)] = pygame.image.load("images/bQueen.png")
piece_to_image[Piece(Type.KING, Color.BLACK)] = pygame.image.load("images/bKing.png")

piece_to_image[Piece(Type.PAWN, Color.WHITE)] = pygame.image.load("images/wPawn.png")
piece_to_image[Piece(Type.BISHOP, Color.WHITE)] = pygame.image.load("images/wBishop.png")
piece_to_image[Piece(Type.KNIGHT, Color.WHITE)] = pygame.image.load("images/wKnight.png")
piece_to_image[Piece(Type.ROOK, Color.WHITE)] = pygame.image.load("images/wRook.png")
piece_to_image[Piece(Type.QUEEN, Color.WHITE)] = pygame.image.load("images/wQueen.png")
piece_to_image[Piece(Type.KING, Color.WHITE)] = pygame.image.load("images/wKing.png")

chessboard = pygame.image.load("images/chessboard480.jpg")
chessboard = pygame.transform.scale(chessboard, (pwidth * 8, pheight * 8))

for piece in piece_to_image.keys():
    piece_to_image[piece] = pygame.transform.scale(piece_to_image[piece], (pwidth, pheight))

# myimage = piece_to_image[Piece(Type.PAWN, Color.BLACK)]
# myimage = pygame.transform.scale(myimage, (100, 100))
# imagerect = myimage.get_rect()

# setup game
game = Game()
x1, y1 = None, None


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click()


def handle_mouse_click():
    mposx, mposy = pygame.mouse.get_pos()
    x, y = mposx // pwidth, 7 - mposy // pheight
    global x1, y1
    if game.board.get(x, y) is not None and game.current_player_color() == game.board.get(x, y).color:
        # If a piece is selected of the player turn's color it gets highlighted and waits until the next click
        # selecting a piece of own color overrides all previous clicks
        x1, y1 = x, y
        return
    if x1 is not None and y1 is not None:
        # when a piece has already been selected, and a new area has been selected, then make_move is called
        print("from:", (x1, y1), "to:", (x, y))
        game.make_move(x1, y1, x, y)
        render()
        game.make_move(*minimax.get_best_move(game.board, 1, game.AI_color))
        x1, y1 = None, None
        render()


def render():
    screen.fill(BACK_COLOR)
    screen.blit(chessboard, (0, 0))
    for x in range(8):
        for y in range(8):
            piece = game.board.get(x, y)
            #     current_player_color = game.current_player_color()
            #     print("current player: " + current_player_color.name)
            #     print(game.board)
            #     x1, y1 = map(int, input("enter your move start : x1, y1").split())
            #     x2, y2 = map(int, input("enter your move end   : x2, y2").split())
            #     game.make_move(x1, y1, x2, y2)

            if check_valid_moves.is_in_check(game.board, Color.WHITE):
                if len(check_valid_moves.moves_while_in_check(game.board, Color.WHITE)) == 0:
                    print("BLACK WON")
                    break

            if check_valid_moves.is_in_check(game.board, Color.BLACK):
                if len(check_valid_moves.moves_while_in_check(game.board, Color.BLACK)) == 0:
                    print("WHITE WON")
                    break

            if check_valid_moves.is_in_check(game.board, game.current_player_color()):
                king = game.board.search(Piece(Type.KING, game.current_player_color()))
                pygame.draw.rect(screen, (255, 0, 0, 0.2),
                                 (king[0][0] * pwidth, (7 - king[0][1]) * pheight, pwidth, pheight), 5)

            if x1 is not None and y1 is not None and x == x1 and y == y1:
                pygame.draw.rect(screen, SELECT_COLOR, (x * pwidth, (7 - y) * pheight, pwidth, pheight))
                pos = check_valid_moves.valid_moves(x, y, game.board)

                moves = [i for i in check_valid_moves.ultimate_check(x, y, game.board, game.current_player_color())
                         if i in pos]
                for tup in moves:
                    c = game.board.copy()
                    c.move_piece(x, y, tup[0], tup[1])
                    if not check_valid_moves.is_in_check(c, game.current_player_color()):
                        pygame.draw.rect(screen, (255, 0, 0, 0.2),
                                         (tup[0] * pwidth, (7 - tup[1]) * pheight, pwidth, pheight), 3)

            if piece is not None:
                screen.blit(piece_to_image[piece], (x * pwidth, (7 - y) * pheight))
    pygame.display.update()


while True:
    clock.tick(60)
    events()
    render()
