import tkinter as tk
from tkinter import *
import math

root = Tk()
root.geometry("700x600")
root.resizable(True, True)
root.config(bg='#2F3136')
root.overrideredirect(True)

root.minimized = False
root.maximized = False

def move(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def minimize():
    root.attributes("-alpha",0) # so you can't see the window when is minimized
    root.minimized = True 

def maximize():

    if root.maximized == False: # if the window was not maximized
        root.normal_size = root.geometry()
        expand_button.config(text=" 🗗 ")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        # now it's maximized
        
    else: # if the window was maximized
        expand_button.config(text=" 🗖 ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized
        # now it is not maximized

title_bar = Frame(root, bg = '#2F3136', relief = 'raised')
title_bar.pack(side=TOP, fill=BOTH)

title = Label(title_bar, text = 'Random Texturepack Generator', bg = '#2F3136', fg = "#F0F0F0")
title.pack(side=RIGHT)

title_bar.bind('<B1-Motion>', move)

close_button = Button(title_bar, text='  ✖  ', font = 'Fredoka-Bold', command = root.destroy, bg = '#2F3136', fg = "red")
close_button.pack(side=LEFT)

min_button = Button(title_bar, text='  ➖  ', font = 'Fredoka-Bold', command = minimize, bg = '#2F3136', fg = "yellow")
min_button.pack(side=LEFT)

expand_button = Button(title_bar, text='  🗖  ', font = 'Fredoka-Bold', command = maximize, bg = '#2F3136', fg = "green")
expand_button.pack(side=LEFT)

root.mainloop()