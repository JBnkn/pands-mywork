# randomGenerator.py
# author: Joseph Benkanoun
# write a program that prints a random number between 1 and 10

import random

x = int(input("Please select the first number: "))
y = int(input("Please select the second number: "))
number = random.randint(x,y)
print(f"here is a random number between {x} and {y}: {number}")