from tkinter import *
from tkinter import ttk
import random

root = Tk()
style = ttk.Style()
style.configure('allowance', background="#f9f9f9ff")
allowance = ttk.Label(root, text="Allowance app")
allowance.grid(column=0, row=0, columnspan=3, rowspan=6, pady=10, padx=10)

root.title("Allowance app")
root.configure(background='lavender')
root.mainloop()
