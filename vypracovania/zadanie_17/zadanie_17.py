# Zadanie 17

# Napíš program, ktorý zašifruje text v súbore pre zadaný číselný kľúč. Každé písmeno zo vstupného súboru zašifruje tak, že znak nahradíte znakom posunutým o daný počet písmen vpravo.

kluc = int(input("Zadaj kluc: "))

text = "Velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium."

encrypted_text = ""

for i in text:
    encrypted_text += chr(ord(i)+kluc)

print(encrypted_text)