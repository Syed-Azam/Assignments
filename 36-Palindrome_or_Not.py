# Ai Assignment 36 - Check Whether Given Input Is Palindrome Or Not
t = input("Enter Text : ")
l = len(t)
p = ""
for n in range(l): # First We will create Palindrome
    p += t[l-n-1]
if t.upper() == p.upper():
    print("Yes! This is a Palindrome!")
else:
    print("No! This is not a Palindrome!")