from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    root.destroy()

def clock():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))

    txt.set(time)

    root.after(1000,clock)

root = Tk()
root.attributes("-fullscreen",False)
root.configure(background='white')
root.bind("x",quit)
root.after(1000,clock)

fnt = font.Font(family='Helvetica', size=120, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='black', background='white')
# lbl = tkinter.Label(text="Test", fg="black", bg="white")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
