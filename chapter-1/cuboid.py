"""
Author: Nattapong Sindhu
CS 101

Programming Exercise 1.5
Program: cuboid.py
Compute the volume of a cuboid.

1. Constants: none
2. Inputs:
     height
     width
     depth
3. Computations:
     volume = height * width * depth
4. The outputs are
     The volume of a cuboid in cubic units.
"""

height = float(input("Enter the height: "))
width = float(input("Enter the width: "))
depth = float(input("Enter the depth: "))
volume = height * width * depth
print("The volume is", volume, "cubic units.")
