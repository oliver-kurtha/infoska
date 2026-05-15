# Zadanie 20

# Vygeneruj 20-prvkové pole záporných čísel. Napíš program, ktorý opakovane pre zadaný index i a hodnotu h pripočíta k prvku s indexom i hodnotu h. Na záver overte, či je pole konštantné.

from random import randint

pole = []
for i in range(10):
    pole.append(randint(-99,-1))

print(pole)
i = int(input("Zadaj index i: "))
h = int(input("Zadaj hodnotu h: "))
pole[i] += h
print(pole)

konstantne = True
for i in range(len(pole)-1):
    if i != i+1:
        konstantne = False

if konstantne:
    print("Pole je konstantne")
else:
    print("Pole nie je konstantne")