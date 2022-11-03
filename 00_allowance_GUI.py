from tkinter import *
from tkinter import ttk
# embeds font into the code for use
from matplotlib import font_manager

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


# Allowance class
class NewWindow:
    pass


class AllowanceGUI:
    def __init__(self):
        super().__init__()

        app_width = 350
        app_height = 600

        resolution = str(app_width) + "x" + str(app_height)

        root = Tk()
        root.geometry(resolution)

        # puts image in the corner of the page
        logo = PhotoImage(file=r"growth.png")
        logo = logo.subsample(7, 7)
        root.iconphoto(False, logo)

        # makes help icon show up on GUI
        help = PhotoImage(file=r"help (1).png").subsample(2, 2)

        # adding style to elements on the GUI
        style = ttk.Style()
        style.configure('allowance', background="#f9f9f9ff")
        style.configure('frame1', background="#f9f9f9ff")
        style.configure('frame1_header', )

        outer_frame = ttk.Frame(root, width=app_width, height=app_height)
        outer_frame.grid(column=0, row=0)

        # Frame 1, encompasses the entire page
        frame1 = ttk.Frame(outer_frame)
        frame1.grid(column=0, row=1, sticky="NSEW", pady=10)
        # A separate frame for the help icon
        frame1_logo = ttk.Label(frame1, image=logo)
        frame1_header = ttk.Label(frame1, text="Ranui Moni", font=('Comfortaa', 20))  # A separate frame for the header
        frame1_logo.grid(column=2, row=0, pady=0, padx=0, sticky="NSEW")
        frame1_header.grid(column=2, row=1, pady=0, padx=0, sticky="NSEW")

        frame2 = ttk.Frame(outer_frame)
        frame2.grid()

        # Creating a photoImage object to use image
        nikaupho = PhotoImage(file=r"jellyfish.png")
        hanapho = PhotoImage(file=r"fox.png")
        tiapho = PhotoImage(file=r"whale.png")

        # Resizing image to fit on button
        nikaupho.subsample(4, 4)
        hanapho.subsample(4, 4)
        tiapho.subsample(4, 4)

        root.title("Allowance app")
        root.configure()
        root.mainloop()


AllowanceGUI()
