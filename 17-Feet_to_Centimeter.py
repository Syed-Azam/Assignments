# Ai Assignment 17 - Convert Height (In Feet And Inches) To Centimetres.
f = int(input("Enter Height : (Feet)   : "))
i = float(input("             : (Inches) : "))
c = ((f * 12) + i) * 2.54
print("Height in Centimeters   :", c, "cm")