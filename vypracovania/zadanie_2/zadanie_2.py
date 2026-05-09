# Zadanie 2

# Napíš program, ktorý bude na obrazovke zobrazovať náhodný tip dňa. Program náhodne vyberie z pripraveného textového súboru reťazec. Vybraný reťazec sa bude postupne zobrazovať od pravej strany obrazovky k ľavej strane. Ak sa reťazec dostane až k ľavej strane obrazovky, znovu sa objaví vpravo.


# tkinter init
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()

tipy = []
f = open("sample.txt", "r")
while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    tipy.append(line)

from random import choice
text = choice(tipy)

x = 803
def tip():
    global x
    canvas.delete("all")
    if x <= 0:
        x = 803
    x -= 3
    canvas.create_text(x, 400, text=text)
    canvas.after(5, tip)

tip()

root.mainloop()
