# Ai Assignment 02 - Check number is positive, negative or zero
num = input("Koi Adad Dakhil Karein : ")
try:
    num = float(num)
    if num > 0:
        print("Wah! :) Yeh Ek Masbat Adad Hai")
    elif num == 0:
        print("Oh! Yeh To Khali Sifar Hai")
    elif num < 0:
        print("Shit! :( Yeh To Ek Manfi Adad Hai")
except ValueError:
    print ("Yeh Mujhe Koi Adad Nahi Lag Raha")