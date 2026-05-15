# Zadanie 15

# Napíš program, ktorý v Morseovom kóde vypíše telegram uložený v textovom súbore. Morseova abeceda je uložená v textovom súbore nasledovným spôsobom: A.-. Napíš program, ktorý pre zadané písmeno vypíše jeho morseový kód, postupne prečíta zo zadaného súboru jednotlivé písmená a prepíše ich do morseovho kódu.

f = open("sample.txt", "r")

codes = []
while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    line = [line[0], line[1:]]
    codes.append(line)

pismeno = input("Zadaj pismeno: ").upper()

for i in codes:
    if pismeno == i[0]:
        print(f"Morseovy kod pre pimeno {pismeno} je {i[1]}")
        break

f = open("sample_2.txt", "r")
text = f.readline().strip()
f.close()

final_text = ""
for i in text:
    morse = False
    for j in codes:
        if i == j[0]:
            final_text += j[1]
            morse = True
            continue
    if not morse:
        final_text += i

f = open("sample_3.txt", "w")
f.write(final_text)
f.close()