import tkinter as tk
from tkinter import *
import math

root = Tk()
root.geometry("700x600")
root.resizable(True, True)
root.config(bg='#2F3136', cursor = "plus")
root.overrideredirect(True)
root.eval('tk::PlaceWindow . center')

root.minimized = False
root.maximized = False

def move(event):
    root.geometry('+{0}+{1}'.format(event.x_root - 350, event.y_root - 10))

def maximize():

    if root.maximized == False: # if the window was not maximized
        root.normal_size = root.geometry()
        expand_button.config(text="   🗗   ")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        # now it's maximized
        
    else: # if the window was maximized
        expand_button.config(text="   🗖   ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized
        # now it is not maximized

def generateCommand():
    print("Generating...")

title_bar = Frame(root, bg = '#2F3136', relief = 'raised')
title_bar.pack(side=TOP, fill=BOTH)

title = Label(title_bar, text = 'Random Texturepack Generator', bg = '#2F3136', fg = "#F0F0F0")
title.pack(side=RIGHT)

title_bar.bind('<B1-Motion>', move)

close_button = Button(title_bar, text='  ❌  ', command = root.destroy, bg = '#2F3136', fg = "red")
close_button.pack(side = LEFT)

expand_button = Button(title_bar, text='   🗖   ', command = maximize, bg = '#2F3136', fg = "green")
expand_button.pack(side = LEFT)

root.loadimage1 = tk.PhotoImage(file="button.png")
root.generateButton = tk.Button(root, image=root.loadimage1, activebackground='#2F3136', cursor = "tcross", command = generateCommand)
root.generateButton["bg"] = "#2F3136"
root.generateButton["border"] = "0"
root.generateButton.pack(side = BOTTOM, pady = 50)

root.loadimage2 = tk.PhotoImage(file="tags.png")
root.tagsButton = tk.Label(root, image=root.loadimage2, activebackground='#2F3136')
root.tagsButton["bg"] = "#2F3136"
root.tagsButton["border"] = "0"
root.tagsButton.pack(side = TOP, pady = 10)

tagsBox = Text(root, height = 10 , width = 5)

root.mainloop()