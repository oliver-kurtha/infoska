# Zadanie 21

# Vytvor program, ktorý simuluje preteky 10 lodičiek. Na obrazovke sa vypíše číslo lodičky, ktorá bola prvá.

import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(width=1000, height=1000, highlightthickness=0)
canvas.pack()

lodicky = []
for i in range(10):
    lodicky.append(0)

canvas.create_rectangle(900,0,920,1000,fill="black")

koniec = False

def zavod():
    global koniec
    if koniec:
        return
    canvas.delete("all")
    canvas.create_rectangle(900,0,905,800,fill="black")
    for i in range(10):
        lodicky[i] += randint(2,10)
        x = lodicky[i]
        y = i * 80 + 80
        canvas.create_rectangle(x,y,x+50,y+15,fill="red")
        if lodicky[i] >= 850:
            print(f"vyhrala lodicka {i+1}")
            koniec = True
    canvas.after(20, zavod)


zavod()


root.mainloop()