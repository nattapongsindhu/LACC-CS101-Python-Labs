"""
Program: bouncy.py

Compute the total distance traveled by a bouncing ball.

1. Significant constants
        none
2. The inputs are
        initial height from which the ball is dropped
        bounciness index of the ball
        number of times the ball is allowed to continue bouncing
3. Computations:
        total distance = initial drop
                         + for each bounce: up (height * index) + down (height * index)
                         except the last bounce only counts the upward distance
4. The outputs are
        total distance traveled in units
"""

# Request the inputs
height = float(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

# Compute total distance
distance = height
currentHeight = height * index

for i in range(bounces):
    if i < bounces - 1:
        distance += 2 * currentHeight
    else:
        distance += currentHeight  # last bounce: up only
    currentHeight *= index

# Display the result
print("\nTotal distance traveled is:", distance, "units.")
