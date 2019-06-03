# Ai Assignment 35 - Find The Number of Notes (Sample Of Notes:
#                    10, 20, 50, 100, 500, And 1000 )
a = int(input("Enter Amount : "))
n = [1000, 500, 100, 50, 20, 10]
for i in n:
    print(i, ":", a // i)
    while a >= i:
        a -= i
    
