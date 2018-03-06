# CTI-110
# P3T1
#  - Calculates the area of two rectangles.
#  - Prints which rectangle has greater area.
# 2018-03-06
#

import math

## Data structures
class Rectangle:
    length = 0
    width = 0

    # Constructs a rectangle of the specified width and height.
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    # Returns the area of the rectangle.
    def getArea(self):
        return self.length * self.width

    # Returns a signed integer (-1, 0, or 1) representing the comparison
    # of the areas of two Rectangle objects.
    def compareArea(self, other):
        difference = self.getArea() - other.getArea()

        return clamp(difference, -1, 1)

# End data structures
    
## Utility methods

# Clamps a value to a the range specified, inclusive.
def clamp(value, minValue, maxValue):
    return min(maxValue, max(value, minValue))
    
# Displays 'prompt' and reads an integer.
#
# Correctly handles erroneous input. Numbers must be greater than zero.
#
# Returns the integer.
def readInteger(prompt):
    stringValue = input(prompt)
    try:
        numberValue = int(stringValue)

        # Ensure the number is greater than zero. If not, try again.
        if numberValue <= 0:
            print("Bad input. Please enter a positive integer.")
            return readNumber(prompt)

        return numberValue
    except:
        # The user entered a non-numerical value. Try again.
        print("Bad input. Please enter a number.")
        return readNumber(prompt)

# Gets the dimensions for rectangle 'name'.
#
# Returns a Rectangle object with the dimensions specified. The width
# and height will be greater than zero.
def readRectangle(name):
    # This closure eliminates repeating the format string.
    def readExtent(extent):
        prompt = "Enter the {} for Rectangle {}: ".format(extent, name)
        return readInteger(prompt)

    # Read dimensions.
    length = readExtent("length")
    width = readExtent("width")

    # Construct rectangle.
    return Rectangle(length, width)

# End utility methods

## Program logic
### Constants
COMPARE_LESS    = -1 # The value is less than the other.
COMPARE_EQUAL   =  0 # The value is equal to the other.
COMPARE_GREATER =  1 # The value is greater than the other.

### Variables

# The rectangles to compare.
rectangleA = None
rectangleB = None

# The result of the area comparison.
comparisonResult = 0

# Get the rectangles.
rectangleA = readRectangle("A")
rectangleB = readRectangle("B")

# Compare them, using 'A' as the reference.
comparisonResult = rectangleA.compareArea(rectangleB)

if comparisonResult == COMPARE_LESS:
    print("Rectangle A has less area than Rectangle B.")
elif comparisonResult == COMPARE_EQUAL:
    print("Rectangle A has equal area to Rectangle B.")
elif comparisonResult == COMPARE_GREATER:
    print("Rectangle A has greater area than Rectangle B.")
else:
    print("I'm melting! Expected COMPARE_*, got {}.".format(comparisonResult))
