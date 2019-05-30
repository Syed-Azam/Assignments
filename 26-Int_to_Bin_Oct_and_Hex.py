# Ai Assignment 26 - Convert An Integer To Binary, Octal And Hexadecimal Numbers
n = input("Input an Integer Number : ")
try:
   v = int(n)
except ValueError:
   print("That's not an int!")
   quit()
print("Binary : ",bin(v))
print("Octal  : ",oct(v))
print("Hex    : ",hex(v))
