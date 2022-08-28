from tkinter import *
from tkinter import ttk
from tkinter import tkinter.font

import random


class AllowanceGUI:
    def __init__(self):
        root = Tk()
        self.style = ttk.Style()

        self.style.configure('allowance', background="#f9f9f9ff")
        self.allowance = ttk.Label(root, text="Allowance app")
        self.allowance.grid(column=0, row=0, columnspan=3, rowspan=6, pady=10, padx=10)
        self.Font.tuple = (Comfortaa, )
        Desired_font = tkinter.font.Font(family="Comic Sans MS",
                                         size=20,
                                         weight="bold")
        root.title("Allowance app")
        root.configure(background='lavender')
        root.mainloop()
