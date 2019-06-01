# Ai Assignment 34 - Input A Text And Count The Occurrences Of
#                    Vowels And Consonant
t = input("Enter Text : ")
v, c = 0, 0
for n in t:
    if n.upper() in "AEIOU":
        v += 1
    if n.upper() in "BCDFGHJKLMNPQRSTVWXYZ":
        c += 1
print("No. of Vowels    :", v)
print("No. of Consonent :", c)