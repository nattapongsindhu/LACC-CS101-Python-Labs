"""
Program: equilateral.py

Determine whether a triangle is equilateral.

1. Significant constants
        none
2. The inputs are
        length of the first side
        length of the second side
        length of the third side
3. Computations:
        equilateral if all three sides are equal
4. The outputs are
        whether or not the triangle is equilateral
"""

# Request the inputs
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Determine if equilateral
if side1 == side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
