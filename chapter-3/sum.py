"""
Program: sum.py

Receive a series of numbers from the user and compute their sum and average.
User presses Enter with no input to quit.

1. Significant constants
        none
2. The inputs are
        a series of numbers (empty input to quit)
3. Computations:
        sum = total of all numbers entered
        average = sum / count
4. The outputs are
        the sum of the numbers
        the average of the numbers
"""

# Accumulate numbers
total = 0.0
count = 0

while True:
    userInput = input("Enter a number or press Enter to quit: ")
    if userInput == "":
        break
    total += float(userInput)
    count += 1

# Display results
print("")
print("The sum is", total)
if count > 0:
    print("The average is", total / count)
