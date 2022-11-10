from tkinter import *

import os

def btn_clicked():
    print("Button Clicked")

def run_snake():
    os.system('python3 snake.py')

def run_pong():
    os.system('python3 PongFinal.py')

def run_firstgame():
    os.system('python3 firstgame.py')

window = Tk()

window.geometry("900x650")
window.configure(bg = "#200606")
canvas = Canvas(
    window,
    bg = "#200606",
    height = 650,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    405.0, 327.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = run_snake,
    relief = "flat")

b0.place(
    x = 13, y = 162,
    width = 253,
    height = 167)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = run_pong,
    relief = "flat")

b1.place(
    x = 475, y = 162,
    width = 253,
    height = 167)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = run_firstgame,
    relief = "flat")

b2.place(
    x = 256, y = 367,
    width = 253,
    height = 167)

img3 = PhotoImage(file = f"Button.png")
b3 = Button(
    image = img3,
    # text= "CLOSE",
    borderwidth = 0,
    highlightthickness = 0,
    command = window.destroy,
    relief = "flat"
    )
    

b3.place(
    x = 692, y = 451,
    width = 105,
    height = 95)

window.resizable(False, False)
window.mainloop()
