# CTI-110
# P4HW2
#  - Calculates a running total.
# Aaron Bolyard
# 2018-04-10
#

def main_ADB():
    # Variables.
    runningTotal_ADB = 0 # Running total; i.e., the sum of all numbers entered.
    currentValue_ADB = 0 # Current input value.

    # By assigning currentValue 0 initially and checking if currentValue is >= 0,
    # we eliminate needing to repeat fetching user input.
    #
    # Similarly, by summing then receiving next input, we don't have to handle
    # the condition of the current value being < 0 inside the loop as an if
    # statement.
    while currentValue_ADB >= 0:
        runningTotal_ADB += currentValue_ADB
        currentValue_ADB = int(input("Enter a number? "))

    print("Total:", runningTotal_ADB)

main_ADB()
