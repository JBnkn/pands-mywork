# grade.py
# author: Joseph Benkanoun
# read a percentage mark and print the corresponding grade

percent = float(input("Enter the percentage: "))
if percent > 100 or percent < 0:
    print("Please enter a number between 0 and 100")
elif percent < 40:
    print("Fail")
elif percent < 50:
    print("Pass")
elif percent < 60:
    print("Merit 2")
elif percent < 70:
    print("Merit 1")
else:
    print("Distinction")