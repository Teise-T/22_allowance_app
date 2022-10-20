import math
import tkinter as tk
from tkinter import Tk, ttk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
# from tkinter import tkinter.font
from matplotlib import font_manager

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


# Ranui Moni Application

class helpPage:
    def __init__(self):
        super().__init__()
        light_grey = '#F9F9F9'
        dark_grey = '#D4D4D4'
        root = Tk()
        # adding decoration to the elements e.g color or
        style = ttk.Style()

        style.configure("Outer_Frame.TFrame", background=dark_grey)
        style.configure("Inner_Frame.TFrame", background=light_grey)
        style.configure("Header.TFrame", background=light_grey)
        style.configure("Body.TFrame", background=light_grey)
        style.configure("Footer.TFrame", background=light_grey)
        style.configure("Logo.TLabel", background=light_grey)
        style.configure("Title.TLabel", background=light_grey)


        #window dimensions
        screen_height = root.winfo_screenheight()
        screen_width = root.winfo_screenwidth()

        app_width = math.floor(screen_width / 4)  # 384
        app_height = math.floor(screen_height / 2.1)  # 493

        resolution = (str(app_width) + "x" + str(app_height))

        root.title("Ranui Moni - Help")
        root.geometry(resolution)

        # resize image
        logo_image = Image.open("growth.png")
        logo_image = logo_image.resize((45, 45))
        logo = ImageTk.PhotoImage(logo_image)

        title_font = ("Comfortaa", 30)
        subtitle_font = ("Comfortaa", 15)

        outer_frame = ttk.Frame(root, style="Outer_Frame.TFrame", width=app_width, height=app_height)
        outer_frame.grid(row=0, column=0)

        inner_frame = ttk.Frame(outer_frame, style="Inner_Frame.TFrame", width=app_width - 20, height=(app_height - 20))
        inner_frame.grid(row=0, column=0, pady=10, padx=10)

        # frame for title "Help page"
        frame_header = ttk.Frame(inner_frame, style="Header.TFrame", width=(app_width - 20),
                                 height=(math.floor(app_height * 0.1)))
        frame_header.grid(row=0, column=0)

        # frame which holds the logo
        header_logo = ttk.Label(frame_header, style="Logo.TLabel", image=logo)
        header_logo.grid(row=0, column=0)

        # frame to keep all the text inside
        frame_body = ttk.Frame(inner_frame, style="Body.TFrame", width=(app_width - 20),
                               height=(math.floor(app_height * 0.25)))
        frame_body.grid(row=1, column=0)

        # label to keep instructions in
        body_label = ttk.Label(frame_body, style="Title.TLabel", text="Help page", font=title_font)
        body_label.place(x=(app_width / 2.1), y=(app_height * 0.15), anchor="center")

        frame_footer = ttk.Frame(inner_frame, style="Footer.TFrame", width=(app_width - 20),
                                 height=(math.floor(app_height * 0.65) - 20))
        frame_footer.grid(row=2, column=0)

        # variable to store the help instructions/information
        help_info = tk.StringVar(frame_footer, "1. Click on your chosen child's name of whom you want to deposit or "
                                               "withdraw money from \n 2. Enter an amount into the entry box \n 3. If "
                                               "you would like to withdraw the entered amount, press the 'withdraw' "
                                               "button \n 4. If you would like to deposit the entered amount, press the 'deposit' button"
                                               "\n If the child is on track to receiving an end-of-year bonus, "
                                               "Their page will say '[Child's name] is on track!' "
                                               "\n If the child is not on track to receiving an end-of-year bonus, their page will say'[Child's name] is not on track'"
                                               "\n ")
        footer_label = ttk.Label(frame_footer, textvariable=help_info, font=subtitle_font,
                                 wraplength=(app_width - 100), padding=10)

        footer_label.place(x=(app_width / 2.1), y=(app_width * 0.325), anchor="center")

        root.mainloop()


helpPage()
