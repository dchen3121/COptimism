# does this work
import tkinter
from chess import *
from PIL import ImageTk, Image
from chess import *

chessboard = tkinter.Tk()
# Chessboard
img = Image.open('images/chessboard.png')
img = img.resize((600, 600), Image.ANTIALIAS)

img2 = ImageTk.PhotoImage(img)

panel = tkinter.Label(chessboard, image=img2)
panel.pack(side="bottom", fill="both", expand="yes")
# White Pieces
wkingImg = Image.open("images/wKing.png")
wkingImg = wkingImg.resize((48, 48), Image.ANTIALIAS)
wkingImg2 = ImageTk.PhotoImage(wkingImg)

wqueenImg = Image.open("images/wQueen.png")
wqueenImg = wqueenImg.resize((48, 48), Image.ANTIALIAS)
wqueenImg2 = ImageTk.PhotoImage(wqueenImg)

wbishopImg = Image.open("images/wBishop.png")
wbishopImg = wbishopImg.resize((48, 48), Image.ANTIALIAS)
wbishopImg2 = ImageTk.PhotoImage(wbishopImg)

wrookImg = Image.open("images/wRook.png")
wrookImg = wrookImg.resize((48, 48), Image.ANTIALIAS)
wrookImg2 = ImageTk.PhotoImage(wrookImg)

wknightImg = Image.open("images/wKnight.png")
wknightImg = wknightImg.resize((48, 48), Image.ANTIALIAS)
wknightImg2 = ImageTk.PhotoImage(wknightImg)

wpawnImg = Image.open("images/wPawn.png")
wpawnImg = wpawnImg.resize((48, 48), Image.ANTIALIAS)
wpawnImg2 = ImageTk.PhotoImage(wpawnImg)

# Black Pieces
bkingImg = Image.open("images/bKing.png")
bkingImg = bkingImg.resize((48, 48), Image.ANTIALIAS)
bkingImg2 = ImageTk.PhotoImage(bkingImg)

bqueenImg = Image.open("images/bQueen.png")
bqueenImg = bqueenImg.resize((48, 48), Image.ANTIALIAS)
bqueenImg2 = ImageTk.PhotoImage(bqueenImg)

bbishopImg = Image.open("images/bBishop.png")
bbishopImg = bbishopImg.resize((48, 48), Image.ANTIALIAS)
bbishopImg2 = ImageTk.PhotoImage(bbishopImg)

brookImg = Image.open("images/bRook.png")
brookImg = brookImg.resize((48, 48), Image.ANTIALIAS)
brookImg2 = ImageTk.PhotoImage(brookImg)

bknightImg = Image.open("images/bKnight.png")
bknightImg = bknightImg.resize((48, 48), Image.ANTIALIAS)
bknightImg2 = ImageTk.PhotoImage(bknightImg)

bpawnImg = Image.open("images/bPawn.png")
bpawnImg = bpawnImg.resize((48, 48), Image.ANTIALIAS)
bpawnImg2 = ImageTk.PhotoImage(bpawnImg)


def get_chesspiece(x, y):
    newBoard = Board.initial_board()
    pos = newBoard.get(x, y)
    if pos is None:
        return 0
    elif pos.color == Color.WHITE:
        if pos.type == Type.KING:
            return wkingImg2
        elif pos.type == Type.QUEEN:
            return wqueenImg2
        elif pos.type == Type.BISHOP:
            return wbishopImg2
        elif pos.type == Type.ROOK:
            return wrookImg2
        elif pos.type == Type.KNIGHT:
            return wknightImg2
        else:
            return wpawnImg2
    elif pos.color == Color.BLACK:
        if pos.type == Type.KING:
            return bkingImg2
        elif pos.type == Type.QUEEN:
            return bqueenImg2
        elif pos.type == Type.BISHOP:
            return bbishopImg2
        elif pos.type == Type.ROOK:
            return brookImg2
        elif pos.type == Type.KNIGHT:
            return bknightImg2
        else:
            return bpawnImg2


for j in range(0, 8):
    for i in range(0, 8):
        if get_chesspiece(i, j)==0:
            if (i % 2 == 0) and (j % 2 != 0):
                blank = tkinter.Button(chessboard, bg="gray50", height=3, width=6)
                blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
            elif (i % 2 != 0) and (j % 2 == 0):
                blank = tkinter.Button(chessboard, bg="gray50", height=3, width=6)
                blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
            else:
                blank = tkinter.Button(chessboard, bg="white", height=3, width=6)
                blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
        else:
            if (i % 2 == 0) and (j % 2 != 0):
                blank = tkinter.Button(chessboard, bg="gray50", image=get_chesspiece(i, j))
                blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
            elif (i % 2 != 0) and (j % 2 == 0):
                blank = tkinter.Button(chessboard, bg="gray50", image=get_chesspiece(i, j))
                blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
            else:
                blank = tkinter.Button(chessboard, bg="white", image=get_chesspiece(i, j))
                blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")


chessboard.mainloop()
