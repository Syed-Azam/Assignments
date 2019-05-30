# Ai Assignment 30 - Count The Number Occurrence Of A Specific Character In A String
s = input("Input a String    : ")
c = input("Input a Character : ")
cnt = 0
for cc in s:
    if cc == c:
        cnt += 1
print("Number Occurrence is :", cnt)