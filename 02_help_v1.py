from tkinter import Tk, PhotoImage
from tkinter import ttk

# embeds font into the code for use
from matplotlib import font_manager


class HelpGUI:
    def __init__(self):
        super().__init__()

        width = 200
        height = 300

        resolution = str(width) + "x" + str(height)

        root = Tk()
        root.geometry(resolution)

        # puts image in the corner of the page
        self.logo = PhotoImage(file=r"help (1).png")
        self.logo = self.logo.subsample(7, 7)
        root.iconphoto(False, self.logo)

        # Frame 1, encompasses the entire page
        self.frame1_help = ttk.Frame(root)
        # A separate frame for the logo
        self.frame1_logo = ttk.Label(self.frame1_help, image=self.logo)
        # Frame for greyed out instruction/info text
        self.frame1_helpinfo = ttk.Frame(root)

        # adding style to elements on the GUI
        self.style = ttk.Style()
        self.style.configure('allowance', background="#f9f9f9ff")
        self.style.configure('frame1', background="#f9f9f9ff")
        self.style.configure('frame1_header')
        self.style.configure('frame1_helpInfo', background="#e4e4e4ff")

        # specific placing for element via grid
        self.frame1_helpinfo.grid(column=1, row=3, pady=3, padx=(width / 2 - 60))
        self.frame1_help.grid(column=2, row=2, sticky="NSEW")
        self.frame1_logo.grid(column=1, row=0, pady=5, padx=(width / 2 - 40), sticky="NSEW")

        root.title("Help page")
        root.configure()
        root.mainloop()


HelpGUI()



