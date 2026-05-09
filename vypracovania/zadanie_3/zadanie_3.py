# Zadanie 3

# Napíš program na jednoduchú variantu hry obesenec, ktorá funguje nasledovne: hráč postupne háda písmená, ak písmeno uhádol, vypíše sa na všetkých miestach v slove, kde sa nachádza. Hra končí po uhádnutí celého slova.

# zadanie slova
guess_word = input("Zadaj slovo: ")

guess = ""
for i in guess_word:
    guess += "*"

guessed_chars = []
while True:
    print(guess)
    guess_char = input("Zadaj pismeno: ")
    if guess_char in guess_word and guess_char not in guessed_chars:
        guessed_chars.append(guess_char)
    guess = ""
    for i in guess_word:
        if i in guessed_chars:
            guess += i
        else: guess += "*"
    if "*" not in guess:
        print("Slovo: " + guess_word)
        print("Koniec hry")
        break

