# Zadanie 30

# Napíš program, ktorý bude simulovať hru „Pacmann“. Pohyb pacmanna bude nepretržitý a stlačením šípky mením len smer pohybu. Na náhodnej pozícii je umiestnený obrázok, ku ktorému sa musí dostať. Následne sa na inom náhodnom mieste objaví ďalší obrázok a celý proces sa bude opakovať.

import tkinter as tk
from random import randint
from math import sqrt
root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()

direction = [0,1]
x, y = 400,400
def zmen_smer(e):
    global direction, x, y 
    if e.keysym == "Up":
        direction = [0,-1]
    if e.keysym == "Down":
        direction = [0,1]
    if e.keysym == "Left":
        direction = [-1,0]
    if e.keysym == "Right":
        direction = [1,0]
    if e.keysym == "space":
        x, y = 400,400



ciel = [randint(20,780),randint(20,780)]
def zobraz():
    global x, y
    canvas.delete("all")
    x += 3 * direction[0]
    y += 3 * direction[1]
    x2 = ciel[0]
    y2 = ciel[1]
    canvas.create_rectangle(x-10,y-10,x+10,y+10,fill="blue",outline="blue")
    if sqrt((x2-x)**2+(y2-y)**2) <= 15:
        zmen_ciel()
    canvas.create_oval(x2-5,y2-5,x2+5,y2+5,fill="red",outline="red")
    canvas.after(10, zobraz)

def zmen_ciel():
    global ciel
    ciel = [randint(20,780),randint(20,780)]


zobraz()



canvas.bind_all("<KeyPress>", zmen_smer)

root.mainloop()