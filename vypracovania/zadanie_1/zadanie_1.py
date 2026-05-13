# Zadanie 1

# V textovom súbore je v každom riadku zapísaná šírka knihy v cm. Napíš program, ktorý načíta šírku poličky, vypíše, či sa všetky knihy zmestia do jednej poličky, a v prípade, že nie, postupne do jednotlivých riadkov vypisuje obsahy jednotlivých poličiek. Koľko poličiek danej šírky by si potreboval?

f = open("sample.txt", "r")
sirky = []

# zadanie sirky policky
sirka_policky = int(input("Zadaj sirku jednej policky: "))

# zaradenie hodnot z textoveho suboru do pola
while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    sirky.append(int(line))

# zaradovanie do policiek
policky = []
terajsia_policka = []
sirka = 0
for i in sirky:
    if sirka + i <= sirka_policky:
        terajsia_policka.append(i)
        sirka += i
    else:
        policky.append(terajsia_policka)
        terajsia_policka = [i]
        sirka = i

if terajsia_policka != []:
    policky.append(terajsia_policka)

# vypisanie
for i in policky:
    print(i)

print("Pocet policiek: " + str(len(policky)))
