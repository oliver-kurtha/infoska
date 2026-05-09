# Zadanie 7


# Napíšte program na hru „Padajúce písmenká“. Program vygeneruje náhodné písmeno v strede prvého riadku obrazovky, ktoré bude postupne padať. Program končí, ak hráč nestlačí správne písmeno skôr, než sa dostane až na dno obrazovky

import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()

abc = []
for i in range(ord("a"), ord("z") + 1):
    abc.append(chr(i))

from random import *
x = randint(20, 780)
y = 0
char = choice(abc)

def drop():
    global y
    if y >= 800:
        print("Koniec hry")
        return
    canvas.delete("all")
    y += 2
    canvas.create_text(x, y, text=char, font=10, anchor="s")
    canvas.after(10, drop)

def press(e):
    global x, y, char
    if e.keysym == char:
        x = randint(20, 780)
        y = 0
        char = choice(abc)

drop()

canvas.bind_all("<KeyPress>", press)


root.mainloop()