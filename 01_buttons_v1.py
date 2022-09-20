# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Creating a photoimage object to use image
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
Button(root, text='Nikau', image=nikaupho,
       compound=LEFT).pack(side=TOP)
Button(root, text='Hana', image=hanapho,
       compound=LEFT).pack(side=TOP)
Button(root, text='Tia', image=tiapho,
       compound=LEFT).pack(side=TOP)
mainloop()