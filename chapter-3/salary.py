"""
Program: salary.py

Display a salary schedule for teachers in a school district.

1. Significant constants
        none
2. The inputs are
        starting salary
        annual percentage increase
        number of years in the schedule
3. Computations:
        year 1 salary = starting salary
        each subsequent year = previous salary * (1 + increase / 100)
4. The outputs are
        tabular salary schedule with year number and salary
"""

# Request the inputs
salary = float(input("Enter the starting salary: "))
increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

# Display the salary schedule
print()
print("Year Salary")
print("-----------")

current_salary = salary
for year in range(1, years + 1):
    print(f"{year:>2} {current_salary:.2f}")
    current_salary = current_salary * (1 + increase / 100)
