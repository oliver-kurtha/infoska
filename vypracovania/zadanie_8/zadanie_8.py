# Zadanie 8

# Napíš program, ktorý bude simulovať informačnú tabuľu v trolejbuse. V textovom súbore sú v riadkoch názvy zastávok. Napíš program, ktorý vypíše zoznam zastávok pod seba od prvej po poslednú a po stlačení ľubovoľnej klávesy sa zoznam vyroluje hore vždy o jednu zastávku.

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(width=800, height=800, highlightthickness=0)
canvas.pack()

f = open("sample.txt", "r")
stops = []

while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    stops.append(line)

def zobraz():
    canvas.delete("all")
    x = 400
    j = 1
    for i in stops:
        y = j * 22
        canvas.create_text(x, y, text=i, anchor="center", font=12)
        j += 1

def klik(e):
    stops.pop(0)
    zobraz()

zobraz()

canvas.bind("<Button-1>", klik)

root.mainloop()



