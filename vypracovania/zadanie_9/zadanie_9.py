# Zadanie 9

# Napíšte program, ktorý bude simulovať nekonečný prejazd mestom. Vygenerujte a graficky znázornite panorámu mesta (20 rôzne vysokých budov v rade), ktorá sa bude postupne vykresľovať sprava doľava.

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()

# inital list
from random import *
b = []
for i in range(20):
    b.append(randint(200,700))

def mesto():
    global b
    canvas.delete("all")
    x = 0
    for i in b:
        canvas.create_rectangle(x,800-i,x+40,800)
        x += 40
    for i in range(19):
        b[i] = b[i+1]
    b[19] = randint(300,700)
    canvas.after(500, mesto)

mesto()


root.mainloop()
