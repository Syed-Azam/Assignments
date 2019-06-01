# Ai Assignment 32 - Compute The Least Common Multiple of Two Positive Integers
n1 = int(input("Input Integer # 1 : "))
n2 = int(input("Input Integer # 2 : "))
x = n1
y = n2
while(y):
    x, y = y, x % y
print("LCM is : ", (n1 * n2) / x)
