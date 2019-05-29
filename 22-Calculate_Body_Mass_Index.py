# Ai Assignment 22 - Calculate Body Mass Index
#                    BMI = weight (kg) ÷ height (m)^2
print("Body Mass Index Calculation")
w = float(input("Enter Weight (kg) : "))
h = float(input("Enter Height (m)  : "))
print("BMI is :", round(w / (h ** 2), 2))