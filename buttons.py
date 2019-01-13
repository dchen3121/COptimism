'''
Check button
'''

from tkinter import Tk, Label, Button


class Check:
    def __init__(self, master):
        self.master = master
        master.title("CHECK")

        self.label = Label(master, text="CHECK!", font="Helvetica, 20")
        self.label.pack(padx=5, pady=10)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


root = Tk()
root.geometry("400x100+450+300")
my_check = Check(root)
root.mainloop()

'''
Checkmate button
'''

class Checkmate:
    def __init__(self, master):
        self.master = master
        master.title("CHECKMATE")

        self.label = Label(master, text="CHECKMATE!", font="Helvetica, 20")
        self.label.pack(padx=5, pady=10)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


root = Tk()
root.geometry("400x100+450+300")
my_checkmate = Checkmate(root)
root.mainloop()

'''
Choosing between two player mode and one player mode
'''


def single_player():
    return("2+2")


def double_player():
    return("3+3")


class modeOption:
    def __init__(self, master):
        self.master = master
        master.title("Mode Selection")

        def single_restart():
            master.quit()
            single_player()

        def double_restart():
            master.quit()
            double_player()

        self.label = Label(master, text="Game Mode:", font="Helvetica, 20")
        self.label.pack(padx=5, pady=10)

        self.single_button = Button(master, text="Single Player", command=single_restart())
        self.single_button.pack(pady=10)

        self.double_button = Button(master, text="Double Player", command=double_restart())
        self.double_button.pack()


root = Tk()
root.geometry("400x150+450+300")
my_modeoption = modeOption(root)
root.mainloop()

print(my_check)
print(my_checkmate)
print(my_modeoption)
