# Create a digital clock


# Librairies

from tkinter import *
import tkinter.ttk as ttk
import datetime


# Code

gui = Tk(className=' Digital Clock')
gui.geometry("2000x1000") 

now = datetime.datetime.now()

canvas= Canvas(gui, width= 2000, height= 1000, bg="SpringGreen2")
canvas.create_text(700, 350, text="Current date and time : ", fill="black", font=('Helvetica 50 bold'))
tm = canvas.create_text(700,450,text=now.strftime("%Y-%m-%d %H:%M:%S"),fill="black",font=("Helvetica 35 bold"))

def change_time():
    now = datetime.datetime.now()
    canvas.itemconfig(tm, text=now.strftime("%Y-%m-%d %H:%M:%S"))
    canvas.pack()
    canvas.after(100,change_time)

change_time()
gui.mainloop()
 

# Launching