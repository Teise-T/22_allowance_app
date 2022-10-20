from tkinter import *
from tkinter import ttk
# embeds font into the code for use
from matplotlib import font_manager

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


# Allowance class
class AllowanceGUI:
    def __init__(self):
        super().__init__()
        root = Tk()
        root.geometry("350x500")
        root.title("Allowance app")
        root.configure()
        root.mainloop()

        # puts image in the corner of the page
        self.logo = PhotoImage(file=r"growth.png")
        self.logo = self.logo.subsample(7, 7)
        root.iconphoto(False, self.logo)

        # makes help icon show up on GUI
        self.help = PhotoImage(file=r"help (1).png")
        self.help = self.help.subsample(2, 2)

        # adding style to elements on the GUI
        self.style = ttk.Style()
        self.style.configure('allowance', background="#f9f9f9ff")
        self.style.configure('frame1', background="#f9f9f9ff")
        self.style.configure('frame1_header')

        # Frame 1, encompasses the entire page
        self.frame1 = ttk.Frame(root)
        # A separate frame for the logo
        self.frame1_logo = ttk.Label(self.frame1, image=self.logo)
        # A separate frame for the header
        self.frame1_header = ttk.Label(self.frame1, text="Ranui Moni", font=('Comfortaa', 20))

        # A separate frame for the help icon
        self.frame1.grid(column=2, row=2, sticky="NSEW")
        self.frame1_logo.grid(column=1, row=0, pady=5, padx=(350 / 2 - 40), sticky="NSEW")
        self.frame1_header.grid(column=1, row=1, pady=0, padx=(350 / 2 - 80), sticky="NSEW")

    def MainPageButtons(event):


    # Creating a photoImage object to use image
    nikaupho = PhotoImage(file=r"jellyfish.png")
    hanapho = PhotoImage(file=r"fox.png")
    tiapho = PhotoImage(file=r"whale.png")

    # Resizing image to fit on button
    nikaupho = nikaupho.subsample(4, 4)
    hanapho = hanapho.subsample(4, 4)
    tiapho = tiapho.subsample(4, 4)

    # here, image option is used to
    # set image on button
    # compound option is used to align
    # image on LEFT side of button
    # buttons for each child: Nikau, Tia and Hana
    nikau_button = Button(root, text='Nikau', image=nikaupho,
           compound=LEFT).pack(side=TOP)
    tia_button = Button(root, text='Hana', image=hanapho,
           compound=LEFT).pack(side=TOP)
    hana_button = Button(root, text='Tia', image=tiapho,
           compound=LEFT).pack(side=TOP)
    mainloop()




AllowanceGUI()
