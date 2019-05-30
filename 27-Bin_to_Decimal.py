# Ai Assignment 27 - Convert a Binary Number to Decimal Number
b = input("Input a Binary Number : ")
for c in b: # Check if user input is really a binary number
    if not (c == "0" or c == "1"):
        print("That's not a Binary Number!")
        quit()
print("Decimal is :", int(b, 2))