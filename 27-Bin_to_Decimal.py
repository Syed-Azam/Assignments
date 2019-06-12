# Ai Assignment 27 - Convert a Binary Number to Decimal Number
b = input("Input a Binary Number : ")
for c in b: # Check if user input is really a binary number
    if not (c == "0" or c == "1"):
        print("That's not a Binary Number!")
        quit()
l = len(b)
d = 0
for c in range(l):
    d = d + int(b[c]) * (2**(l-c-1))
print("Decimal Equavalent is : ", d)