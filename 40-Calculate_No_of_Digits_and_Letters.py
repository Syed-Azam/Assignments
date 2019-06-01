# Ai Assignment 40 - Accepts A String And Calculate The Number Of
#                    Digits And Letters Sample Data
t = input("Input String : ")
v, c = 0, 0
for n in t:
    if n.upper() in "0123456789":
        v += 1
    if n.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c += 1
print("No. of Letters :", c)
print("No. of Digits  :", v)