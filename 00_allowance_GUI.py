from tkinter import *
from tkinter import ttk
# embeds font into the code for use
from matplotlib import font_manager


font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


# Allowance class
class AllowanceGUI:
    def __init__(self):
        root = Tk()
        root.geometry("350x500")

        # puts image in the corner of the page
        self.logo = PhotoImage(file=r"growth.png")
        self.logo = self.logo.subsample(7, 7)
        root.iconphoto(False, self.logo)

        # makes help icon show up on GUI
        self.help = PhotoImage(file=r"help (1).png")
        self.help = self.help.subsample(2, 2)
        #

        # adding style to elements on the GUI
        self.style = ttk.Style()
        self.style.configure('allowance', background="#f9f9f9ff")
        self.style.configure('frame1', background="#f9f9f9ff")
        self.style.configure('frame1_header', )

        # Frame 1, encompasses the entire page
        self.frame1 = ttk.Frame(root)
        # A separate frame for the logo
        self.frame1_logo = ttk.Label(self.frame1, image=self.logo)
        # A separate frame for the header
        self.frame1_header = ttk.Label(self.frame1, text="Ranui Moni", font=('Comfortaa', 20))
        self.label2 = ttk.Label(self.frame1)
        # A separate frame for the help icon
        # self.frame1_help =
        self.frame1.grid(column=2, row=2, sticky="NSEW")
        self.frame1_logo.grid(column=1, row=0, pady=5, padx=(350 / 2 - 40), sticky="NSEW")
        self.frame1_header.grid(column=1, row=1, pady=0, padx=(350 / 2 - 80), sticky="NSEW")
        self.label2.grid(column=0, row=1)

        root.title("Allowance app")
        root.configure()
        root.mainloop()


AllowanceGUI()
