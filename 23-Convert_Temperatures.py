# Ai Assignment 23 - Convert Tempretures to and from Celsius,Fahrenheit
def line():
    print("▬"*42)
line()
print("Tempretures Conversion Program")
line()
print("(1) From Celsius to Fahrenheit")
print("(2) From Fahrenheit to Celsius")
line()
c = input("Enter Your Choice [1/2] : ")
t = float(input("Enter Tempreture....... : "))
line()
if c == "1":
    r = t * (9 / 5) + 32
    print(t, "Celsius is equal to", r, "Fahrenheit")
elif c == "2":
    r = (t - 32) * (5 / 9)
    print(t, "Fahrenheit is equal to", r, "Celsius")
line()