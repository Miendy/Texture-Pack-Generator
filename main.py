import tkinter as tk
import pyautogui as pg
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("700x600")
# root.attributes('-transparentcolor', '#2F3136')
root.config(bg='#2F3136', cursor = "plus")
root.overrideredirect(True)
root.eval('tk::PlaceWindow . center')

root.minimized = False
root.maximized = False

def move(event):
    root.geometry('+{0}+{1}'.format(event.x_root - 350, event.y_root - 15))

def maximize():

    if root.maximized == False: # if the window was not maximized
        root.normal_size = root.geometry()
        expand_button.config(text="   🟢   ")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        
    else:
        expand_button.config(text="   🟡   ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized

def generateCommand():
    idea_file = open('tags.txt', 'r')
    idea_file.readline().splitlines()
    print(idea_file)

title_bar = Frame(root, bg = '#2F3136', relief = 'raised')
title_bar.pack(side=TOP, fill=BOTH)

title = Label(title_bar, text = 'Random Texturepack Idea Generator   ', bg = '#2F3136', fg = "#F0F0F0")
title.pack(side = RIGHT)

title_bar.bind('<B1-Motion>', move)

close_button = Button(title_bar, text='  🔴  ', command = root.destroy, bg = '#2F3136', fg = "red")
close_button.pack(side = LEFT)

expand_button = Button(title_bar, text='   🟡   ', command = maximize, bg = '#2F3136', fg = "yellow")
expand_button.pack(side = LEFT)

root.loadimage1 = tk.PhotoImage(file="generate.png")
root.generateButton = tk.Button(root, image=root.loadimage1, activebackground='#2F3136', cursor = "exchange", command = generateCommand)
root.generateButton["bg"] = "#2F3136"
root.generateButton["border"] = "0"
root.generateButton.pack(side = BOTTOM, pady = 50)

root.loadimage2 = tk.PhotoImage(file="tags.png")
root.tagsButton = tk.Label(root, image=root.loadimage2)
root.tagsButton["bg"] = "#2F3136"
root.tagsButton["border"] = "0"
root.tagsButton.pack(side = TOP, pady = 30)

frame = Frame(root, width = 500, height = 300, borderwidth = 0, highlightthickness = 0, background = '#2F3136')
frame.pack()
frame.place(anchor = 'center', relx = 0.5, rely = 0.4)

txtWallpaper = ImageTk.PhotoImage(Image.open("text.png"))

imageLabel = Label(frame, image = txtWallpaper, bd = 0)
imageLabel.pack()

menu = StringVar()
menu.set("Select Diffucalty")

dropDown = OptionMenu(root, menu, "Easy", "Medium", "Hard", "Impossible")
dropDown.config(bg = "#2F3136", activebackground = "#2F3136", highlightthickness = 0)
dropDown.pack(side = BOTTOM)

root.mainloop()