# CTI-110
# M4LAB1
#  - Draws a square and then a rectangle.
#  - You could also say it draws a house like a kid.
#    It's just missing the stick people.
# 2018-03-27
#

import turtle
import math

def main_ADB():
    # Create window to draw into.
    window_ADB = turtle.Screen()

    # Great A'tuin, from Discworld.
    # It's a turtle that the Discworld rests upon.
    # Well, it's a turtle with four elephants on
    # its back which themselves are holding up the
    # Discworld...
    atuin_ADB = turtle.Turtle()

    # Draw a square.
    #
    # A square are four equal length sides with an
    # interior angle of 90 degrees.
    for i in range(0, 4):
        atuin_ADB.forward(50)
        atuin_ADB.right(90)

    # Draw an equilateral triangle.
    #
    # An equilateral triangle has an interior of
    # 60 degrees, with each side the same length.
    #
    # However, we are moving along the exterior of
    # the shape; thus, we must move (180 - angle)
    # so that the interior angle is correct.
    for i in range(0, 3):
        atuin_ADB.forward(50)
        atuin_ADB.left(120)

    # Looks like a house. :)
    window_ADB.mainloop()

main_ADB()
