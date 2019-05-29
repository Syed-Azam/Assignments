# Ai Assignment 24 - Sum Of The First N Positive Integers
n = int(input("Input a Number : "))
s = 0
for t in range(n+1):
    print(t)
    s += t
print("Sum Of The First",n ," Positive Integers are : ",s)