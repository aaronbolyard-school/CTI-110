# CTI-110
# P4HW1
#  - Shows a table of the distance traveled.
# Aaron Bolyard
# 2018-04-10
#

import math

def main_ADB():
    # Variables.
    speedMPH_ADB         = 0 # Speed, in miles-per-hour, as a float.
    numHoursTraveled_ADB = 0 # Number of hours traveled, as an integer

    # Get user input.
    speedMPH_ADB = float(input("What is the speed of the vehicle in mph? "))
    numHoursTraveled_ADB = int(input("How many hours has it traveled? "))

    # Print table. Use table to separate columns.
    print("Hour", "Distance Traveled", sep='\t')
    print("---------------------------")

    for hour_ADB in range(1, numHoursTraveled_ADB + 1):
        # Calculate the number of miles traveled, rounding to neareat integer as
        # necessary.
        distanceTraveled_ADB = math.floor(hour_ADB * speedMPH_ADB + 0.5)

        print(hour_ADB, distanceTraveled_ADB, sep='\t')

main_ADB()
