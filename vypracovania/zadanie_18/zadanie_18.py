# Zadanie 18

# Napíš program, ktorý zadaný reťazec vypíše v binárnom tvare.

text = input("Zadaj text: ")

final_text = ""
for i in text:
    cislo = ord(i)
    binarne = str(format(cislo, "08b")) + " "
    final_text += binarne

print(final_text.strip())