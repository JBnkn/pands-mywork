# guess1.py
# author: Joseph Benkanoun
# prompts the user to guess a number and keep prompting the user to guess until the user gets it right

import random

number = random.randint(1,100)

guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess > number:
        print("Guess lower!")
    else:
        print("Guess higher!")
    guess = int(input("Guess a number between 1 and 100: "))
else:
    print(f"Correct! The number was {number}")