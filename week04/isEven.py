# isEven.py
# author: Joseph Benkanoun
# program to prompt an input number and check if it is Odd or Even

number = int(input("Enter an integer: "))

while number != -1:
    if (number % 2) == 0:
        print(f"{number} is an Even number")
    else:
        print(f"{number} is an Odd number")
    number = int(input("Enter an integer: "))