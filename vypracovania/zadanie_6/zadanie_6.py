# Zadanie 6

# V textovom súbore hada.txt máme zapísaný priebeh hier „Háďa“. V každom riadku je zapísaný priebeh jednej hry. V riadku sú znaky, ktoré reprezentujú smer pohybu Háďaťa (H - hore, D - dole, L - vľavo, P - vpravo). Jeden znak symbolizuje jeden krok v danom smere. Vytvorte program, ktorý zistí počet zapísaných hier v súbore, najdlhšiu hru a vytvorí kópiu súboru v komprimovanom tvare použitím metódy opakujúcich sa znakov.

f = open("sample.txt", "r")
g = []
while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    g.append(line)

najdlhsia_hra = 0
najvacia_dlzka = 0
f = open("komprimovane.txt", "w")
d = 0
for i in g:
    d += 1
    if len(i) > najvacia_dlzka:
        najdlhsia_hra = d
        najvacia_dlzka = len(i)
    x = 0
    letter = i[0]
    comp = ""
    for j in i:
        if letter == j:
            x += 1
        else: 
            comp += str(x) + letter
            x = 1
        letter = j
    comp += str(x) + letter
    f.write(comp + "\n")

print("Pocet hier je " + str(len(g)))
print("Najdlhsia hra je " + str(najdlhsia_hra))
