# normalise.py
# author: Joseph Benkanoun
# read a string, remove leading/trailing spaces, convert to lower case
# output length of input and output

input = str(input("Please enter a string: "))
input_len = len(input)
trimmed = input.strip().lower()
output_len = len(trimmed)
print(f"That String normalised is: {trimmed}\nWe reduced the input string from {input_len} to {output_len} characters.")