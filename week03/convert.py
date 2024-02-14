# round.py
# author: Joseph Benkanoun
# take a float amount in dollars and output absolute amount in cent

dollars = float(input("Please enter an amount: "))
dollar_str = str(abs(dollars))
cents = dollar_str.replace(".", "")
print(f"That amount in cent is: {cents}")

# used replace method as found on W3Schools
# there's probably a cleaner method to simply delete a character
# but it worked for now