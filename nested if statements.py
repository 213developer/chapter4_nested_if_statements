"""
EmployeeBonus.py - This program calculates an employee's productivity bonus.
"""

# Initialize variables here.
BONUS_1 = 50.00
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

employeeName = input("Enter employee's name: ")
shiftString = input("Enter number of shifts: ")
transactString = input("Enter number of transactions: ")
dollarString = input("Enter transactions dollar value: ")

numShifts = float(shiftString)
numTransactions = float(transactString)
dollarValue = float(dollarString)

# Write your code here
# A productivity score is dividing an employees transactions dollar value by the number of transactions and then dividing the result by the number of shifts worked
bonus = (dollarValue/numTransactions)/

# Output.
# print(productivityScore)
print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))
