import sys
import os

from game import Game
from chess import *
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
width, height, = 1000, 1000
pwidth, pheight = 100, 100
BACK_COLOR = (255, 255, 255)
SELECT_COLOR = (110, 110, 200)
POSSIBLE_COLOR = (110, 110, 200)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# load images for the pieces
piece_to_image = {}
piece_to_image[Piece(Type.PAWN, Color.BLACK)] = pygame.image.load("bPawn.png")
piece_to_image[Piece(Type.BISHOP, Color.BLACK)] = pygame.image.load("bBishop.png")
piece_to_image[Piece(Type.KNIGHT, Color.BLACK)] = pygame.image.load("bKnight.png")
piece_to_image[Piece(Type.ROOK, Color.BLACK)] = pygame.image.load("bRook.png")
piece_to_image[Piece(Type.QUEEN, Color.BLACK)] = pygame.image.load("bQueen.png")
piece_to_image[Piece(Type.KING, Color.BLACK)] = pygame.image.load("bKing.png")

piece_to_image[Piece(Type.PAWN, Color.WHITE)] = pygame.image.load("wPawn.png")
piece_to_image[Piece(Type.BISHOP, Color.WHITE)] = pygame.image.load("wBishop.png")
piece_to_image[Piece(Type.KNIGHT, Color.WHITE)] = pygame.image.load("wKnight.png")
piece_to_image[Piece(Type.ROOK, Color.WHITE)] = pygame.image.load("wRook.png")
piece_to_image[Piece(Type.QUEEN, Color.WHITE)] = pygame.image.load("wQueen.png")
piece_to_image[Piece(Type.KING, Color.WHITE)] = pygame.image.load("wKing.png")

chessboard = pygame.image.load("chessboard480.jpg")
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
        x1, y1 = x, y
        return
    if x1 is not None and y1 is not None:
        print("from:", (x1, y1), "to:", (x, y))
        game.make_move(x1, y1, x, y)  # the move was not valid
        x1, y1 = None, None
        render()


def render():
    screen.fill(BACK_COLOR)
    screen.blit(chessboard, (0, 0))
    for x in range(8):
        for y in range(8):
            piece = game.board.get(x, y)
            if x1 is not None and y1 is not None and x == x1 and y == y1:
                pygame.draw.rect(screen, SELECT_COLOR, (x * pwidth, (7 - y) * pheight, pwidth, pheight))
            if
            if piece is not None:
                screen.blit(piece_to_image[piece], (x*pwidth, (7 - y)*pheight))
    pygame.display.update()


while True:
    clock.tick(60)
    events()
    render()
