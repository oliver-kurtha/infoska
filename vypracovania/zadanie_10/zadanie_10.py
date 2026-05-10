# Zadanie 10

# Napíšte program, ktorý nakreslí mriežku k piškvorkám pre zadaný počet riadkov/stĺpcov. Veľkosť jedného štvorčeka je 10x10. Následne ľavým tlačidlom myši kreslíme do zadaného štvorčeka krížik, pravým tlačidlom kreslíme krúžok. Zabezpeč, aby si hráči navzájom nemohli prepísať už označené políčka a aby sa striedali.

riadky = int(input("Zadaj pocet riadkov: "))
stlpce = int(input("Zadaj pocet stlpcov: "))

width, height = stlpce * 50, riadky * 50

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(width=width, height=height, highlightthickness=0)
canvas.pack()

for i in range(riadky-1):
    x = width
    y = i * 50 + 50
    canvas.create_line(0,y,x,y)

for i in range(stlpce-1):
    x = i * 50 + 50
    y = height
    canvas.create_line(x,0,x,y)

obsadene_policka = []

cross = True
def cross(e):
    global cross
    x1 = e.x//50*50 + 10
    y1 = e.y//50*50 + 10
    if cross and [x1,y1] not in obsadene_policka:
        x2, y2 = x1 + 30, y1 + 30
        canvas.create_line(x1,y1,x2,y2)
        canvas.create_line(x1+30,y1,x1,y2)
        obsadene_policka.append([x1,y1])
        cross = False

canvas.bind("<Button-1>", cross)

def oval(e):
    global cross
    x1 = e.x//50*50 + 10
    y1 = e.y//50*50 + 10
    if not cross and [x1,y1] not in obsadene_policka:
        x2, y2 = x1 + 30, y1 + 30
        canvas.create_oval(x1,y1,x2,y2)
        obsadene_policka.append([x1,y1])
        cross = True

canvas.bind("<Button-3>", oval)




root.mainloop()