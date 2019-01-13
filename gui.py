# does this work
import tkinter
from chess import *
from PIL import ImageTk, Image

chessboard = tkinter.Tk()
# Chessboard
img = Image.open('chessboard.png')
img = img.resize((600, 600), Image.ANTIALIAS)

img2 = ImageTk.PhotoImage(img)

panel = tkinter.Label(chessboard, image=img2)
panel.pack(side="bottom", fill="both", expand="yes")
# White Pieces
wkingImg = Image.open("wKing.png")
wkingImg = wkingImg.resize((48, 48), Image.ANTIALIAS)
wkingImg2 = ImageTk.PhotoImage(wkingImg)

wqueenImg = Image.open("wQueen.png")
wqueenImg = wqueenImg.resize((48, 48), Image.ANTIALIAS)
wqueenImg2 = ImageTk.PhotoImage(wqueenImg)

wbishopImg = Image.open("wBishop.png")
wbishopImg = wbishopImg.resize((48, 48), Image.ANTIALIAS)
wbishopImg2 = ImageTk.PhotoImage(wbishopImg)

wrookImg = Image.open("wRook.png")
wrookImg = wrookImg.resize((48, 48), Image.ANTIALIAS)
wrookImg2 = ImageTk.PhotoImage(wrookImg)

wknightImg = Image.open("wKnight.png")
wknightImg = wknightImg.resize((48, 48), Image.ANTIALIAS)
wknightImg2 = ImageTk.PhotoImage(wknightImg)

wpawnImg = Image.open("wPawn.png")
wpawnImg = wpawnImg.resize((48, 48), Image.ANTIALIAS)
wpawnImg2 = ImageTk.PhotoImage(wpawnImg)

# Black Pieces
bkingImg = Image.open("bKing.png")
bkingImg = bkingImg.resize((48, 48), Image.ANTIALIAS)
bkingImg2 = ImageTk.PhotoImage(bkingImg)

bqueenImg = Image.open("bQueen.png")
bqueenImg = bqueenImg.resize((48, 48), Image.ANTIALIAS)
bqueenImg2 = ImageTk.PhotoImage(bqueenImg)

bbishopImg = Image.open("bBishop.png")
bbishopImg = bbishopImg.resize((48, 48), Image.ANTIALIAS)
bbishopImg2 = ImageTk.PhotoImage(bbishopImg)

brookImg = Image.open("bRook.png")
brookImg = brookImg.resize((48, 48), Image.ANTIALIAS)
brookImg2 = ImageTk.PhotoImage(brookImg)

bknightImg = Image.open("bKnight.png")
bknightImg = bknightImg.resize((48, 48), Image.ANTIALIAS)
bknightImg2 = ImageTk.PhotoImage(bknightImg)

bpawnImg = Image.open("bPawn.png")
bpawnImg = bpawnImg.resize((48, 48), Image.ANTIALIAS)
bpawnImg2 = ImageTk.PhotoImage(bpawnImg)


def get_chesspiece(x, y):
    pos = board.get(x, y)
    if pos.color == Color.WHITE:
        if pos.type == Type.KING:
            chesspiece = wkingImg2
        elif pos.type == Type.QUEEN:
            chesspiece = wqueenImg2
        elif pos.type == Type.BISHOP:
            chesspiece = wbishopImg2
        elif pos.type == Type.ROOK:
            chesspiece = wrookImg2
        elif pos.type == Type.KNIGHT:
            chesspiece = wknightImg2
        else:
            chesspiece = wpawnImg2
    else:
        if pos.type == Type.KING:
            chesspiece = bkingImg2
        elif pos.type == Type.QUEEN:
            chesspiece = bqueenImg2
        elif pos.type == Type.BISHOP:
            chesspiece = bbishopImg2
        elif pos.type == Type.ROOK:
            chesspiece = brookImg2
        elif pos.type == Type.KNIGHT:
            chesspiece = bknightImg2
        else:
            chesspiece = bpawnImg2


for j in range(0, 8):
    for i in range(0, 8):
        if (i % 2 == 0) and (j % 2 != 0):
            blank = tkinter.Button(chessboard, bg="gray50", image=get_chesspiece(i, j))
            blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
        elif (i % 2 != 0) and (j % 2 == 0):
            blank = tkinter.Button(chessboard, bg="gray50", height=3, width=6)
            blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")
        else:
            blank = tkinter.Button(chessboard, bg="white", height=3, width=6)
            blank.place(relx=.13 + (i * .105), rely=.135 + (j * .102), anchor="c")


'''wKing = tkinter.Button(chessboard, image = wkingImg2)
wQueen = tkinter.Button(chessboard, image = wqueenImg2)
wBishop = tkinter.Button(chessboard, image = wbishopImg2)
wRook = tkinter.Button(chessboard, image = wrookImg2)
wKnight = tkinter.Button(chessboard, image = wknightImg2)

wKing.place(relx=.13+(i*.105), rely=.24, anchor="c")
wQueen.place(relx=.13+(i*.105), rely=.24, anchor="c")
wBishop.place(relx=.13+(i*.105), rely=.24, anchor="c")
wRook.place(relx=.13+(i*.105), rely=.24, anchor="c")
wKnight.place(relx=.13+(i*.105), rely=.24, anchor="c")

for i in range (0, 8):
    wPawn = tkinter.Button(chessboard, image = wpawnImg2)
    wPawn.place(relx=.13+(i*.105), rely=.24, anchor="c")'''

chessboard.mainloop()
