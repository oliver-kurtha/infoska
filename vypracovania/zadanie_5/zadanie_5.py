# Zadanie 5

# Vygeneruj a vykresli náhodnú krajinu. Náhodne vyber smer stúpania alebo klesania a bod zlomu. Postupne generuj a vykresľuj neklesajúcu alebo nerastúcu lomenú čiaru až po bod zlomu a následne zmeňte smer stúpania alebo klesania. Oblasť pod lomenou čiarou vyfarbi náhodným odtieňom zelenej.


import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(width=800, height=500, highlightthickness=0)
canvas.pack()

from random import *
zlom = randint(20, 60) 
y = randint(200, 300) # vyska
d = choice([1, -1]) # smer
points = [(0, 500), (0, y)] # prve dva body
x = 0
# generacia bodov
for i in range(1,81):
    x += 10
    y += randint(1,5) * d
    points.append([x, y])
    if i == zlom: 
        d *= -1 # otocenie smeru

# posledny pod, nalavo dole
points.append((800,500))

# vykresli
canvas.create_polygon(points, fill=f"#00{randint(100,255):02x}00")



root.mainloop()