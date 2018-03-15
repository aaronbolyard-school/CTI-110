# CTI-110
# P3T1
#  - Calculates the area of two rectangles.
#  - Prints which rectangle has greater area.
# 2018-03-06
#

# Variables.
length1_ADB = 0
length2_ADB = 0
width1_ADB = 0
width2_ADB = 0

# Get the length of width of two rectangles.
length1_ADB = int(input("Enter length of first rectangle: "))
width1_ADB = int(input("Enter width of first rectangle: "))
length2_ADB = int(input("Enter length of second rectangle: "))
width2_ADB = int(input("Enter width of second rectangle: "))

# Compute the length of each rectangle, as defined by the formula 'a = l * w'
# (where 'l' is length and 'w' is width).
area1_ADB = length1_ADB * width1_ADB
area2_ADB = length2_ADB * width2_ADB

if area1_ADB > area2_ADB:
    print("The area of the first rectangle is greatest.")
else:
    if area2_ADB > area1_ADB:
        print("The area of the second rectangle is greatest.")
    else:
        print("The area of the rectangles are equal.")
