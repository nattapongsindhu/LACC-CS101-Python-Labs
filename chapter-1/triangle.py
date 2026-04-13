"""
Author: Nattapong Sindhu
CS 101

Programming Exercise 1.3
Program: triangle.py
Compute the area of a triangle.

1. Constants: none
2. Inputs:
     base
     height
3. Computations:
     area = .5 * base * height
4. The outputs are
     The area of a triangle in square units.
"""

base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = .5 * base * height
print("The area is", area, "square units.")
