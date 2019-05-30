# Ai Assignment 29 - Convert a Hexadecimal Number to Decimal Number
b = input("Input an Hexadecimal Number : ")
for c in b: # Check if user input is really an Hexadecimal number
    if not (c.upper() in "0123456789ABCDEF"):
        print(c)
        print("Please Enter a Valid Hexadecimal Number!")
        quit()
print("Decimal is :", int(b, 16))