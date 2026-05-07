import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()

suradnice = []

for i in range(50):
    suradnice.append([390, randint(0, 780)])

def pohyb():
    canvas.delete("all")
    for i in suradnice:
        if i[1] % 2 == 0:
            i[0] -= 10
            if i[0] <= -20:
                i[0] = 800
        else:
            i[0] += 10
            if i[0] >= 800:
                i[0] = -20
        x,y=i[0],i[1]

        canvas.create_rectangle(x,y,x+20,y+20,fill="red")
    canvas.after(20, pohyb)

pohyb()


root.mainloop()