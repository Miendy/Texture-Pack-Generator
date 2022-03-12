import tkinter as tk
from tkinter import *
import math

root = Tk()
root.title("Random Texturepack Generator")
root.geometry("700x600")
root.resizable(False, False)
root.config(bg='#2F3136')
root.overrideredirect(True)

def move(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

title_bar = Frame(root, bg = '#2F3136', relief = 'raised', bd = 2)
title_bar.pack(side=LEFT)

title = Label(title_bar, text = 'x', bg = '#2F3136', fg = "red")
title.pack(side=LEFT)

title_bar.bind('<B1-Motion>', move)

root.mainloop()