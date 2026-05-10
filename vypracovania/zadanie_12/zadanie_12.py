# Zadanie 12

# V riadkoch textového súboru je uložené slovenské slovo a pomlčkou oddelený jeho preklad do anglického jazyka. Pre zadané slovo vypíš jeho preklad. Postupne prejdi obsah celého súboru a vymaž chybné riadky.

f = open("sample.txt", "r")

preklady = []

while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    preklad = line.split("-")
    preklady.append(preklad)

sk_word = input("zadaj slovenske slovo: ")

for i in preklady:
    if i[0] == sk_word:
        print("preklad: " + i[1])

for i in preklady:
    print("sk: " + i[0])
    print("en: " + i[1])
    to_delete_input = input("vymazat? y/n ")
    if to_delete_input == "y":
        preklady.remove(i)


f = open("slovnik.txt", "w")

for i in preklady:
    f.write(i[0]+"-"+i[1]+"\n")


