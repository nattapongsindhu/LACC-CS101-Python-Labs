"""
Program: right.py

Determine whether a triangle is a right triangle.

1. Significant constants
        none
2. The inputs are
        length of the first side
        length of the second side
        length of the third side
3. Computations:
        sort sides so the largest is the hypotenuse
        right triangle if a^2 + b^2 == c^2 (Pythagorean theorem)
4. The outputs are
        whether or not the triangle is a right triangle
"""

# Request the inputs
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Sort sides so largest is hypotenuse
sides = sorted([side1, side2, side3])
a, b, c = sides[0], sides[1], sides[2]

# Determine if right triangle
if a ** 2 + b ** 2 == c ** 2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
