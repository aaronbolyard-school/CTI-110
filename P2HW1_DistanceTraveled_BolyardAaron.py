# CTI-110
# P2HW1: Calculates the distance traveled over certain periods.
# Aaron Bolyard
# 2018-02-20

# The speed, in miles-per-hour.
SPEED = 70

# The travel time, in hours.
TIMES = [ 6, 10, 15 ]

# Prints the computed distance based on the speed and time parameters.
def print_distance_traveled(speed, time):
    distance = speed * time
    print("...in {} hour(s), the car traveled {} miles.".format(time, distance))

print("Assuming {} MPH...".format(SPEED))

# Iterate over times and print distance.
for i in TIMES:
    print_distance_traveled(SPEED, i)
