import tkinter as tk
from tkinter import *
import math

root = Tk()
root.geometry("700x600")
root.resizable(False, False)
root.config(bg='#2F3136')
root.overrideredirect(True)

def move(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def minimize1():
    root.state(newstate='iconic')

def maximize():
    root.state(newstate='normal')

title_bar = Frame(root, bg = '#2F3136', relief = 'raised')
title_bar.pack(side=TOP, fill=BOTH)

title = Label(title_bar, text = 'Random Texturepack Generator', bg = '#2F3136', fg = "#F0F0F0")
title.pack(side=RIGHT)

title_bar.bind('<B1-Motion>', move)

close_button = Button(title_bar, text='  x  ', font = 'Fredoka-Bold', command = root.destroy, bg = '#2F3136', fg = "red")
close_button.pack(side=LEFT)

min_button = Button(title_bar, text='  -  ', font = 'Fredoka-Bold', command = minimize1, bg = '#2F3136', fg = "red")
min_button.pack(side=LEFT)

root.mainloop()