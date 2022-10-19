import math
import tkinter
from tkinter import Tk, ttk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
# from tkinter import tkinter.font
from matplotlib import font_manager


font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Ranui Moni Application

class help_page:
    def __init__(self):
        super().__init__()

        light_grey = '#F9F9F9'
        dark_grey = '#D4D4D4'
         help_info.StringVar("")

        root = Tk()
        # adding decoration to the elements e.g color or
        style = ttk.Style()

        style.configure("Outer_Frame.TFrame", background=dark_grey)
        style.configure("Header.TFrame", background=light_grey, foreground='red')
        style.configure("Body.TFrame", background=light_grey)
        style.configure("Footer.TFrame", background=light_grey)

        style.configure("Logo.TLabel", background=light_grey)
        style.configure("Title.TLabel", background=light_grey)

        screen_height = root.winfo_screenheight()
        screen_width = root.winfo_screenwidth()

        app_width = math.floor(screen_width / 4) # 384
        app_height = math.floor(screen_height / 1.7) # 493

        resolution = (str(app_width) + "x" + str(app_height))

        root.title("Ranui Moni - Help")
        root.geometry(resolution)

        logo_image = Image.open("growth.png")
        logo_image = logo_image.resize((45, 45))
        logo = ImageTk.PhotoImage(logo_image)

        title_font = ("Consolas", 30)
        subtitle_font = ("Consolas", 15)

        outer_frame = ttk.Frame(root, style="Outer_Frame.TFrame", width=app_width, height=app_height)
        outer_frame.grid(row=0, column=0)

        inner_frame = ttk.Frame(outer_frame, width=app_width - 20, height=(app_height - 20))
        inner_frame.grid(row=0, column=0, pady=10, padx=10)

        frame_header = ttk.Frame(inner_frame, style="Header.TFrame", width=(app_width - 20), height=(math.floor(app_height * 0.1)))
        frame_header.grid(row=0, column=0)

        header_logo = ttk.Label(frame_header, style="Logo.TLabel", image=logo)
        header_logo.grid(row=0, column=0)

        frame_body = ttk.Frame(inner_frame, style="Body.TFrame", width=(app_width - 20), height=(math.floor(app_height * 0.25)))
        frame_body.grid(row=1, column=0)

        body_label = ttk.Label(frame_body, style="Title.TLabel", text="Help page", font=title_font)
        body_label.place(x=(app_width / 2.1), y=(app_height * 0.15), anchor="center")

        frame_footer = ttk.Frame(inner_frame, style="Footer.TFrame", width=(app_width - 20), height=(math.floor(app_height * 0.65) - 20))
        frame_footer.grid(row=2, column=0)

        footer_label = ttk.Label(frame_footer, text="f,jvn sd\n4. Do some stuff", font=subtitle_font, wraplength=(app_width - 100), padding=10)
        footer_label.place(x=(app_width / 2.1), y=(app_width * 0.325), anchor="center")


        root.mainloop()

help_page()