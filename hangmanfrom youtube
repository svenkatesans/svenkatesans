import random
import os

import words as words

with open('wordlists.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]
allowederrors = int(input("the the number of error that you wanted to be allowed"))
guesses = []
q = False
while not q:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("")
    guess = input(f"Allowered ERRORS LEFT{allowederrors},Next guess:")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowederrors -= 1
        if allowederrors == 0:
            break
    q = True
    for letter in word:
        if letter.lower() not in guesses:
            q = False

if q :
    print ("game won")
else:
    print("loss")

