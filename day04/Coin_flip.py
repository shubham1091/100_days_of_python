"""
You are going to write a virtual coin toss program.
It will randomly tell the user "Heads" or "Tails".
"""
import random
flip = random.randint(0, 1)

if flip == 1:
    print("Heads")
else:
    print("Tails")
