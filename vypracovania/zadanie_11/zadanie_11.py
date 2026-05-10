# Zadanie 11

# Vygeneruj 20-prvkovú neklesajúcu postupnosť čísel. Pre zadané číslo vypíš index jeho výskytu. V prípade, že sa číslo v postupnosti nenachádza, vypíš dva po sebe idúce indexy, medzi ktorými by sa mohol nachádzať.

from random import randint

postupnost = []
for i in range(20):
    postupnost.append(randint(1,100))

postupnost.sort()
print(postupnost)

num = int(input("Zadaj cislo: "))

if num in postupnost:
    print("Cislo " + str(num) + " sa nachadza na indexe " + str(postupnost.index(num)))
else:
    for i in postupnost:
        if num < i:
            print("Cislo sa nachadza medzi indexami " + str(postupnost.index(i)-1) + " a " + str(postupnost.index(i)))
            break