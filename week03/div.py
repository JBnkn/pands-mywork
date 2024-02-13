# div.py
# author: Joseph Benkanoun
# write a program that divides the first number by the second

first = int(input("Enter first number: "))
second = int(input("Enter the number you want to divide by: "))
integer = first//second
remainder = first%second
print(f"{first} divided by {second} is {integer} with remainder {remainder}")