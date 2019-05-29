# Ai Assignment 25 - Sum Of The Digits In An Integer
n = input("Input a Integer Number : ")
try:
   v = int(n)
except ValueError:
   print("That's not an int!")
   quit()
n = str(abs(int(n))) # dealing with negative value
s = 0
for d in n:
    s += int(d)
print("Sum of the Digits are :", s)