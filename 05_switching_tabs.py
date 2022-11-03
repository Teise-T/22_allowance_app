# Multi-frame tkinter application v2.3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from matplotlib import font_manager

font_manager.findSystemFonts(fontpaths=None, fontext="ttf")


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

        self.app_height = 600
        self.app_width = 350

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # tk.Frame.__init__(self, master)
        # tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        # tk.Button(self, text="Return to start page",
        #           command=lambda: master.switch_frame(StartPage)).pack()

        app_width = master.app_width
        app_height = master.app_height

        print(app_width)
        print(app_height)

        style = ttk.Style()

        style.configure('Outer_Frame.TFrame', background='#E4E4E4')
        style.configure('Inner_Frame.TFrame', background='#F9F9F9')
        style.configure('Frame_Header.TFrame', background='red')

        style.configure('Nikau.TButton', lightcolor='red')

        style.configure('Frame_Footer.TFrame', background='blue')

        style.configure('allowance', background="#f9f9f9ff")
        style.configure('frame1', background="#f9f9f9ff")
        # style.configure('frame1_header', )

        outer_frame = ttk.Frame(self, style='Outer_Frame.TFrame', width=350, height=600)
        outer_frame.grid(column=0, row=0)

        inner_frame = ttk.Frame(self, style='Inner_Frame.TFrame', width=(app_width - 20), height=(app_height - 20))
        inner_frame.grid(column=0, row=0)

        frame_header = ttk.Frame(inner_frame, style='Frame_Header.TFrame', width=(app_width - 20),
                                 height=((app_height - 20) * 0.3))
        frame_header.grid(column=0, row=0)

        header_image = ttk.Label(frame_header, image=logo, width=(app_width - 20))
        header_image.grid(column=0, row=0)

        header_label = ttk.Label(frame_header, text='Ranui Moni', font=('Comfortaa', 20))
        header_label.grid(column=0, row=1)

        frame_body_top = ttk.Frame(inner_frame, width=(app_width - 20), height=((app_height - 20) * 0.2))
        frame_body_middle = ttk.Frame(inner_frame, width=(app_width - 20), height=((app_height - 20) * 0.2))
        frame_body_bottom = ttk.Frame(inner_frame, width=(app_width - 20), height=((app_height - 20) * 0.2))

        frame_body_top.grid(column=0, row=1)
        frame_body_middle.grid(column=0, row=2)
        frame_body_bottom.grid(column=0, row=3)

        # frame_body = ttk.Frame(inner_frame, style='Inner_Frame.TFrame', width=(app_width - 20), height=((app_height - 20) * 0.6))
        # frame_body.grid(column=0, row=0)

        # Creating and resizing a photoImage object to use image
        nikaupho = PhotoImage(file=r"jellyfish.png").subsample(4, 4)
        hanapho = PhotoImage(file=r"fox.png").subsample(4, 4)
        tiapho = PhotoImage(file=r"whale.png").subsample(4, 4)

        ttk.Button(frame_body_top, text='Nikau', image=nikaupho, compound=LEFT, width=34,
                   command=master.switch_frame(StartPage)).grid(column=0, row=1)
        ttk.Button(frame_body_middle, text='Hana', image=hanapho, compound=LEFT, width=34).grid(column=0, row=2)
        ttk.Button(frame_body_bottom, text='Tia', image=tiapho, compound=LEFT, width=34).grid(column=0, row=3)

        frame_footer = ttk.Frame(inner_frame, style='Footer_Frame.TFrame', width=(app_width - 20),
                                 height=((app_height - 20) * 0.1))
        frame_footer.grid(column=0, row=4)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()

    app_width = 350
    app_height = 600
    resolution = str(app_width) + "x" + str(app_height)

    logo = PhotoImage(file=r"growth.png")
    logo = logo.subsample(7, 7)
    app.iconphoto(False, logo)

    app.geometry(resolution)
    app.mainloop()
