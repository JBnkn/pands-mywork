# average.py
# author: Joseph Benkanoun
# keep reading numbers until the user enters a 0
# program should append each of them into a list
# program should then print out each of the numbers entered and the average of them

numbers = []

number = int(input("Enter a number (type 0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter a number (type 0 to quit): "))

for n in numbers:
    print(n)

average = float(sum(numbers))/len(numbers)
print(f"The average is {average}")