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
productivityScore = (dollarValue/numTransactions)/numShifts

if productivityScore >= 200.00:
    bonus = BONUS_4
elif (productivityScore >= 70) and (productivityScore <= 199):
    bonus = BONUS_3
elif (productivityScore >= 31) and (productivityScore <= 69):
    bonus = BONUS_2
elif productivityScore <= 30:
    bonus = BONUS_1

# Output.
print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))
