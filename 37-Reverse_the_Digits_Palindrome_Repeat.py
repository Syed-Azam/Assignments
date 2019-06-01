# Ai Assignment 37 - Reverse The Digits Of A Given Number And Add It To The
#                    Original, If The Sum Is Not A Palindrome Repeat
n = int(input("Enter Digit : "))
while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
print(n)