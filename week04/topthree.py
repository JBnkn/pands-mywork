# topthree.py
# author: Joseph Benkanoun
# generate 10 random numbers (0-100), prints them out, then print out the top three

import random

numbers = []

while len(numbers) <10:
    num = random.randint(0,100)
    numbers.append(num)

print(numbers) 
numbers.sort(reverse = False)
print(numbers[0:3])