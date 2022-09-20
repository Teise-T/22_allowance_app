from tkinter import *
from tkinter import ttk
# from tkinter import tkinter.font
from matplotlib import font_manager

from PIL import Image, ImageTk

img = ImageTk.PhotoImage(Image.open("growth.png"))

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


class AllowanceGUI:
    def __init__(self):
        root = Tk()
        root.geometry("350x500")
        self.logo = PhotoImage(file="growth.png")
        self.style = ttk.Style()
        self.style.configure('allowance', background="#f9f9f9ff")
        self.style.configure('frame1', background="#f9f9f9ff")
        self.frame1 = ttk.Frame(root)
        self.frame1.grid(column=0, row=0, columnspan=4, rowspan=10, sticky="NSEW")
        self.label1 = ttk.Label(self.frame1, text="Ranui Moni", font="Comfortaa")
        self.label1.grid(column=2, row=0, pady=20, padx=20, sticky="NSEW")
        self.label2 = ttk.Label(self.frame1)
        self.label2.grid(column=0, row=1)
        root.title("Allowance app")
        root.configure()
        root.mainloop()


AllowanceGUI()
