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


print(my_check)
print(my_checkmate)