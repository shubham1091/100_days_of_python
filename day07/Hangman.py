import random
import os
import art
from word import word_list

def show():
    for i in display:
        print(i,end=" ")
    print()

print(art.logo)

choosen_word = random.choice(word_list)

# print(f"pssst, the solution is {choosen_word}")

display = ['_']*len(choosen_word)
show()
live = len(art.stage)-1
no_hint = 3
while True:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    if guess == "hint" and no_hint > 0:
        print("There is '", random.choice(choosen_word), "' in the word")
        no_hint -= 1
        continue
    elif len(guess) > 1:
        print("Only one letter")
        continue
    change = 0
    if guess in display:
        print("You have already guessed this letter")
        continue
    
    for i in range(len(display)):
        if guess == choosen_word[i]:
            display[i] = guess
            change += 1

    if change == 0:
        print(f"you guessed the letter {guess}, that's not in the word. you lost a life")
        live -= 1
    print(art.stage[live])
    show()
    if '_' not in display:
        print("You won")
        break
    if live == 0:
        print("You lost")
        break
if live >0:
    print("well done")
else:
    print(f"better luck next time\nthe correct answer was {choosen_word}")