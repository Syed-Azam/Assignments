# Ai Assignment 20 - Convert All Units Of Time Into Seconds
print("Convert All Units Of Time Into Seconds")

d = int(input("Input days: ")) * 60 * 60 * 24
h = int(input("Input hours: ")) * 60 * 60
m = int(input("Input minutes: ")) * 60
s = int(input("Input seconds: "))

t = d + h + m + s

print("The  amounts of seconds", t)