"""
Program: momentum.py

Compute an object's momentum and kinetic energy.

1. Significant constants
        none
2. The inputs are
        mass (in kilograms)
        velocity (in meters per second)
3. Computations:
        momentum = mass * velocity
        kinetic energy = (1/2) * mass * velocity^2
4. The outputs are
        the object's momentum
        the object's kinetic energy
"""

# Request the inputs
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# Compute the momentum and kinetic energy
momentum = mass * velocity
kineticEnergy = 0.5 * mass * velocity ** 2

# Display the results
print("The object's momentum is " + str(momentum))
print("The object's kinetic energy is " + str(kineticEnergy))
