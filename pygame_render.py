import sys
import os

from game import Game
from chess import *
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
width, height, = 1000, 1000
pwidth, pheight = 100, 100
back_color = (255, 255, 255)
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
    print(x, y)


def render():
    screen.fill(back_color)
    screen.blit(chessboard, (0, 0))
    for x in range(8):
        for y in range(8):
            piece = game.board.get(x, y)
            if piece is not None:
                screen.blit(piece_to_image[piece], (x*100, y*100))
            # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x*100, y*100, 90, 90))
    # imagerect = pygame.Rect(0, 0, 300, 300)
    # screen.blit(myimage, imagerect)
    pygame.display.update()


while True:
    clock.tick(60)
    events()
    render()
