# Zadanie 19

# V textovom súbore sú uložené značky áut a suma za priestupok, ktorého sa vodiči dopustili. Napíšte program, ktorý pre zadanú značku overí, či sa v súbore nachádza a zistí počet priestupkov a celkovú dlžnú sumu pre danú značku. Zistí celkový počet rôznych EČV v súbore.

f = open("sample.txt", "r")

pokuty = []
while True:
    line = f.readline().split()
    if line == []:
        f.close()
        break
    line[1] = int(line[1])
    pokuty.append(line)

ecv = input("Zadaj ECV: ")

pokuta = 0
pocet = 0
rozne_ecv = []
for i in pokuty:
    if i[0] == ecv:
        pokuta += i[1]
        pocet += 1
    if i[0] not in rozne_ecv:
        rozne_ecv.append(i[0])


if pokuta != 0:
    print(f"Pocet priestupkov pre ECV {ecv}: {pocet}")
    print(f"Hodnota celkovej pokuty: {pokuta}")
else:
    print("Tato ECV nebola najdena")
print(f"Pocet roznych ECV: {len(rozne_ecv)}")


