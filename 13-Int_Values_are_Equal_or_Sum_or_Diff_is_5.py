# Ai Assignment 13 - Integer Values Are Equal Or Their Sum Or Difference Is 5.
n1 = int(input("Enter Integer 1 : "))
n2 = int(input("Enter Integer 2 : "))
if n1 == n2:
    result = True
elif n1 + n2 == 5:
    result = True
elif abs(n1 - n2) == 5:
    result = True
else:
    result = False
    
print(result)