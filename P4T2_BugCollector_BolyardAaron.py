# P4T2
#  - Counts bugs caught in a week.
# Aaron Bolyard
# 2018-03-26

# Constant to store names of days by index.
DAYS_ADB = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturady"
]

def main_ADB():
    total_ADB   = 0 # Total number of bugs.
    average_ADB = 0 # Average number of bugs.

    # For each day, get the number of bugs caught on day.
    # Then increase total by value.
    for day_ADB in range(0, len(DAYS_ADB)):
        numBugsCaught_ADB = int(input("How many bugs did you catch on {}? ".format(DAYS_ADB[day_ADB])))
        total_ADB += numBugsCaught_ADB

    # Compute average.
    average_ADB = total_ADB // len(DAYS_ADB)

    # Print the result.
    print("You caught {0} bugs. That's an average of {1} bug(s) a day.".format(total_ADB, average_ADB))

main_ADB()
