word = input("zadaj slovo: ")

guess_word = ""

for i in word:
    guess_word += "?"

print(guess_word)
 
guessed_chars = []
while True:
    guess = input("pismeno: ")
    if guess in word and guess not in guessed_chars:
        guessed_chars.append(guess)
        guess_word = ""
        for i in word:
            if i in guessed_chars:
                guess_word += i
            else: guess_word += "?"
    print(guess_word)
    if "?" not in guess_word:
        break
        
print("koniec hry!")

