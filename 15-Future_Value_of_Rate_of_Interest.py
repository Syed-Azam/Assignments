# Ai Assignment 15 - Future Value Of A Specified Principal Amount, 
#                    Rate Of Interest, And A Number Of Years
amt = float(input("Enter Amount : "))
interest = float(input("Enter Interest Ratio : ")) 
years = int(input("Enter No. of Years : "))
future_value  = amt * ((1 + (interest/100)) ** years)
print("Future Value is : " + str(round(future_value,2)))
