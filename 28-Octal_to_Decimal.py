# Ai Assignment 27 - Convert an Octal Number to Decimal Number
b = input("Input an Octal Number : ")
for c in b: # Check if user input is really an Octal number
    if not (c in "01234567"):
        print(c)
        print("Please Enter a Valid Octal Number!")
        quit()
print("Decimal is :", int(b, 8))