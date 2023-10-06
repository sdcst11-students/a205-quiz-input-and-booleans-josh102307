"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
n = "no"
n2 = "yes"
x1 = float(input("side 1: "))
x2 = float(input("side 2: "))
hypot = str(input("is one of these numbers the hypotenuse?: "))
if hypot == n:
    answer = (x1**2 + x2**2) **0.5
    print(round(answer,1))
elif hypot == n2:
    x1 >= x2
    answer = x2 / (math.sqrt(2))
    print(round(answer,1))
elif hypot == n2:
    x2 >= x1
    answer = x1 / (math.sqrt(2))
    print(round(answer,1))