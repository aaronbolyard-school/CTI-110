# M4LAB2
#  - Prints initials.
# Aaron Bolyard
# 2018-03-29
#

import turtle
import math

# Size of a letter, in whateer units turtle uses.
LETTER_SPAN_SIZE = 100

# Quality of a circle.
#
# In simple terms, the circle will be drawn with this many segments.
CIRCLE_QUALITY = 10

# Resets the pen to the specified position, with 0 deg heading.
def resetPen_ADB(atuin_ADB, x, y):
    atuin_ADB.penup()
    atuin_ADB.setposition(x, y)
    atuin_ADB.setheading(0)
    atuin_ADB.pendown()

# Prints a partial circle, 'angle' degrees in total.
def printCircle_ADB(atuin_ADB, radius_ADB, angle_ADB):
    circleSegmentLength_ADB = radius_ADB * math.pi / CIRCLE_QUALITY
    for i in range(0, CIRCLE_QUALITY):
        partialAngle_ADB = angle_ADB / CIRCLE_QUALITY
        atuin_ADB.right(partialAngle_ADB)
        atuin_ADB.forward(circleSegmentLength_ADB)

# Prints the letter A.
def printA_ADB(atuin_ADB, size_ADB):
    # Left leg of A
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB)

    # Top of A
    printCircle_ADB(atuin_ADB, size_ADB / 4, 180)

    # Right leg of A
    atuin_ADB.forward(size_ADB)

    # Spanning row of A
    atuin_ADB.penup()
    atuin_ADB.left(180)
    atuin_ADB.forward(size_ADB / 2)
    atuin_ADB.pendown()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 2)

# Prints the letter B.
def printB_ADB(atuin_ADB, size_ADB):
    # Side of B
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB)

    # Top curve of B
    printCircle_ADB(atuin_ADB, size_ADB / 2, 270)

    atuin_ADB.right(90 + 45)

    # Bottom curve of B
    printCircle_ADB(atuin_ADB, size_ADB / 2, 270)

def main_ADB():
    window_ADB = turtle.Screen()
    atuin_ADB = turtle.Turtle()

    atuin_ADB.pensize(20)
    atuin_ADB.pencolor("grey")

    # Draw the A slightly to the left...
    resetPen_ADB(atuin_ADB, -LETTER_SPAN_SIZE / 2, 0)
    printA_ADB(atuin_ADB, LETTER_SPAN_SIZE)

    # ...and the B slightly to the right.
    resetPen_ADB(atuin_ADB, LETTER_SPAN_SIZE / 2, 0)
    printB_ADB(atuin_ADB, LETTER_SPAN_SIZE)

    window_ADB.mainloop()

main_ADB()
