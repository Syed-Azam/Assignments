# Ai Assignment 16 - Distance between two points (X1, Y1) and (X2, Y2)
#                    Distance formula is: SQRT[(X1 - X2)^2 + (Y1 - Y2)^2]
from math import sqrt
x1, y1, x2, y2 = input("Enter [X1 Y1 X2 Y2] Separated by Spaces : ").split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("Distance is : ", d)