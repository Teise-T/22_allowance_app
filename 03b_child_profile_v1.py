from tkinter import *
from tkinter import ttk
import tkinter as Tk
# embeds font into the code for use
from matplotlib import font_manager

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


class NikauProf(root):

    def __init__(self, root=None):
        super().__init__(root=root)
        self.title("Nikau Ranui")
        self.geometry("200x200")
        label = Label(self, text="Nikau bitch")
        label.pack()

        # creates a Tk() object
        root = Tk()

        # sets the geometry of
        # main root window
        root.geometry("200x200")

        label = Label(root, text="This is the main window")
        label.pack(side=TOP, pady=10)

        # a button widget which will
        # open a new window on button click
        btn = Button(root,
                     text="Click to open a new window")

        # Following line will bind click event
        # On any click left / right button
        # of mouse a new window will be opened
        btn.bind("<Button>",
                 lambda e: (root))

        btn.pack(pady=10)


# mainloop, runs infinitely
mainloop()
