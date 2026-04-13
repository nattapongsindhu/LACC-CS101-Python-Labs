"""
Program: employeepay.py

Compute an employee's total weekly pay.

1. Significant constants
        none
2. The inputs are
        hourly wage
        total regular hours
        total overtime hours
3. Computations:
        regular pay = wage * regularHours
        overtime pay = overtimeHours * 1.5 * wage
        total weekly pay = regular pay + overtime pay
4. The outputs are
        the total weekly pay
"""

# Request the inputs
wage = float(input("Enter the wage: $").replace("$", ""))
regularHours = float(input("Enter the regular hours: "))
overtimeHours = float(input("Enter the overtime hours: "))

# Compute the total weekly pay
regularPay = wage * regularHours
overtimePay = overtimeHours * 1.5 * wage
totalPay = regularPay + overtimePay

# Display the total weekly pay
print("The total weekly pay is $" + str(round(totalPay, 2)))
