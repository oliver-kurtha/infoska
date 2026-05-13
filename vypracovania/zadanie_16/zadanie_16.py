# Zadanie 16

# Napíš program, ktorý hráčovi umožní nakresliť obrázok tak, že postupne pospája body v správnom poradí. Body sú zapísané v textovom súbore nasledovným spôsobom. V jednom riadku je zapísané poradové číslo bodu a jeho súradnice.

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(width=900, height=500, highlightthickness=0)
canvas.pack()

f = open("sample.txt", "r")

body = []
while True:
    line = f.readline().split()
    if line == []:
        f.close()
        break
    for i in range(len(line)):
        line[i] = int(line[i])
    body.append(line)

for i in body:
    x = i[1]
    y = i[2]
    canvas.create_oval(x-2,y-2,x+2,y+2,fill="black")
    text = str(i[0])
    canvas.create_text(x-4,y-4,text=text, anchor="e")


root.mainloop()