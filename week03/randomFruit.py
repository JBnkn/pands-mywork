# randomFruit.py
# author: Joseph Benkanoun
# write a program that prints out a random fruit

import random

fruits = ["Apple", "Kiwi", "Banana", "Plum", "Orange"]

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print(f"A random fruit is {fruit}")