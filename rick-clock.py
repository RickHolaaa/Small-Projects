# Create a digital clock


# Librairies

from tkinter import *
import tkinter.ttk as ttk
import time

# Code

gui = Tk(className=' Digital Clock')
gui.geometry("2000x1000") 

#label.place(x=200,y=100,anchor="center")
#label.pack(expand=True)

canvas= Canvas(gui, width= 2000, height= 1000, bg="SpringGreen2")
canvas.create_text(700, 350, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
canvas.pack()



gui.mainloop()
 

# Launching