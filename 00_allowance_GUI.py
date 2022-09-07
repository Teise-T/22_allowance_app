from tkinter import *
from tkinter import ttk
# from tkinter import tkinter.font
from matplotlib import font_manager
import random

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")




class AllowanceGUI:
    def __init__(self):
        root = Tk()
        self.style = ttk.Style()
        self.style.configure('allowance', background="#f9f9f9ff")
        self.style.configure('frame1', background="#f9f9f9ff")
        self.frame1 = ttk.Frame(root)
        self.frame1.grid(columnspan=40, rowspan=50)
        self.label1 = ttk.Label(self.frame1, text="Ranui Moni", font="Comfortaa")
        self.label1.grid(column=0, row=0, pady=20, padx=20, sticky="NSEW")
        self.buttonFrame = ttk.Frame(root)
        self.nButton = ttk.Button(self.)
        self.label2.grid(column=0, row=5, )

        # self.Font.tuple = (Comfortaa, )
        # self.Comfortaa = tkinter.font.Font(family="Comfortaa",
        # size=20,
        # weight="bold")
        root.title("Allowance app")
        root.configure(background='lavender')
        root.mainloop()


AllowanceGUI()
