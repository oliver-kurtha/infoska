import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()


x, y = 385, 385
direction = [1, 0]
ciel_pos = [randint(50, 730), randint(50, 730)]

def pohyb(e):
    global x, y, direction
    if e.keysym == "Right":
        direction = [1,0]
    elif e.keysym == "Left":
        direction = [-1,0]
    if e.keysym == "Down":
        direction = [0,1]
    elif e.keysym == "Up":
        direction = [0,-1]


def zobraz():
    global x, y, ciel_pos
    canvas.delete("all")
    x += direction[0]*5
    y += direction[1]*5
    if abs((x+20) - (ciel_pos[0]+10)) <= 30 and abs((y+20) - (ciel_pos[1]+10)) <= 30:
        zmen_ciel()
    canvas.create_rectangle(x, y, x+40, y+40, fill="red", outline="red")
    canvas.create_oval(ciel_pos[0], ciel_pos[1], ciel_pos[0]+20, ciel_pos[1]+20, fill="blue", outline="blue")
    canvas.after(20, zobraz)


def zmen_ciel():
    global ciel_pos
    ciel_pos = [randint(50, 730), randint(50, 730)]

canvas.bind_all("<KeyPress>", pohyb)

zobraz()
root.mainloop()