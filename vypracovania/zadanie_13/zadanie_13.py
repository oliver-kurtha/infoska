# Zadanie 13

# V textovom súbore si cyklista postupne zaznamenal všetky svoje výlety. V každom riadku súboru je zaznamenaný cieľ, počet prejdených kilometrov a dátum cesty v tvare RRMMDD. Koľkokrát cyklista v roku jazdil? Pre zadaný cieľ vypíš dátumy cesty. Pre každý mesiac vypíš priemerný počet odjazdených kilometrov. 

f = open("sample.txt", "r")
vylety = []

while True:
    line = f.readline().split()
    if line == []:
        f.close()
        break
    line = line[:2] + [" ".join(line[2:])]
    vylety.append(line)


ciel = input("Zadaj ciel: ")

datumy = []
for i in vylety:
    if ciel in i:
        datumy.append(i[0])

mesiace,priemery = [],[]
for i in range(1,13):
    mesiace.append([i])
    priemery.append([i])

for i in vylety:
    mesiac = int(i[0][2:4])
    for j in mesiace:
        if j[0] == mesiac:
            j.append(float(i[1]))


x = 0
for i in mesiace:
    if len(i) == 1:
        priemery[x].append(0)
    else:
        priemery[x].append(round(sum(i[1:]) / (len(i)-1)))
    x += 1

print("Jazdil " + str(len(vylety)) + " krat")
print("S cielom " + ciel + " jazdil v datumoch: " + ", ".join(datumy))
print(priemery)