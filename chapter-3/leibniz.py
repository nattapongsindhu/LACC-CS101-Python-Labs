"""
Program: leibniz.py

Approximate the value of pi using the Leibniz formula.

1. Significant constants
        none
2. The inputs are
        number of iterations
3. Computations:
        pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
        pi = 4 * (sum of series for n iterations)
4. The outputs are
        the approximation of pi
"""

# Request the input
iterations = int(input("Enter the number of iterations: "))

# Compute the approximation of pi
total = 0
for i in range(iterations):
    total += ((-1) ** i) / (2 * i + 1)

pi = 4 * total

# Display the result
print("\nThe approximation of pi is", pi)
