# Zadanie 22

# Napíš program, ktorý pre zadaný reťazec zistí, či je palindrom. Vygeneruj náhodný palindrom pozostávajúci z písmen malej abecedy.

slovo = input("Zadaj retazec: ")

polovica = len(slovo)//2
pol_1 = ""
pol_2 = ""
for i in range(polovica):
    pol_1 += slovo[i]
if len(slovo) % 2 == 1:
    for i in range(polovica+1,polovica*2+1):
        pol_2 += slovo[i]
else:
    for i in range(polovica,polovica*2):
        pol_2 += slovo[i]
pol_2 = "".join(reversed(pol_2))
print(pol_2)
if pol_1 == pol_2:
    print(f"Slovo {slovo} je palindrom!")
else:
    print(f"Slovo {slovo} nie je palindrom :(")

palindrom 



