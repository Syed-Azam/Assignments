# Ai Assignment 31 - Compute The Greatest Common Divisor (Gcd) Of
#                    Two Positive Integers Using Euclidean Algorithm
n1 = int(input("Input Integer # 1 : "))
n2 = int(input("Input Integer # 2 : "))

while True:
    if n1 == 0 or n2 == 0:
        print("GCD is : ",abs(n1 - n2))
        break
    if n1 < n2:
        n1, n2 = n2, n1
    n1 = n1 % n2
