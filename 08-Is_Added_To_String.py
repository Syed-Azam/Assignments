# Ai Assignment 06 - "Is" Added to the Front of a String
s = input("Enter a String : ")
if s[0:2].lower() != "is":
    s = "Is" + s
print("New String is : " + s)