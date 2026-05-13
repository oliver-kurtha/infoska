# Zadanie 14

# V textovom súbore sú uložené trasy liniek mestskej hromadnej dopravy. V jednotlivých riadkoch je zaznamenaná trasa linky v podobe postupnosti jednotlivých zastávok, ktorými linka prechádza. Zisti koľko liniek jazdí v meste a ktorá linka má najdlhšiu trasu. Pre všetky zastávky v meste zisti koľko liniek cez ne prechádza. (mhd.txt)

f = open("sample.txt", "r")

linky = []
while True:
    line = f.readline().split()
    for i in range(len(line)):
        line[i] = int(line[i])
    if line == []:
        f.close()
        break
    linky.append(line)

najdlhsia_linka = 0
dlzka_linky = 0
for i in linky:
    if len(i) > dlzka_linky:
        najdlhsia_linka = linky.index(i)+1
        dlzka_linky = len(i)

zastavky = []
vsetky_zastavky = []

for i in linky:
    for j in i:
        if [j, 0] not in zastavky:
            zastavky.append([j, 0])
        vsetky_zastavky.append(j)

zastavky.sort()

for i in vsetky_zastavky:
    zastavky[i-1][1] += 1

print("Pocet liniek: " + str(len(linky)))
print("Najdlhsia linka: " + str(najdlhsia_linka))
print(zastavky)
