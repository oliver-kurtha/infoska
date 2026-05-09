# Zadanie 4

# V textovom súbore máme 50 rovnakých príkladov uložených v súbore v tvare: + 23 15. Napíš program, ktorý vytvorí z daného súboru dva nové súbory. Jeden súbor bude obsahovať len príklady na sčítanie a druhý na násobenie spolu aj s výsledkami: * 2 12 24. Sú oba súbory rovnako veľké?

f = open("sample.txt", "r")
priklady = []
while True:
    line = f.readline().split()
    if line == []:
        f.close()
        break
    line[1] = int(line[1])
    line[2] = int(line[2])
    priklady.append(line)

f = open("scitanie.txt", "w")
for i in priklady:
    if i[0] == "+":
        i[1] = str(i[1])
        i[2] = str(i[2])
        f.write(" ".join(i) + "\n")

f = open("nasobenie.txt", "w")
for i in priklady:
    if i[0] == "*":
        i.append(i[1] * i[2])
        i[1] = str(i[1])
        i[2] = str(i[2])
        i[3] = str(i[3])
        f.write(" ".join(i) + "\n")
