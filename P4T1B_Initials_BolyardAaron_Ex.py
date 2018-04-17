# CTI-110
# P4T1B
#  - Prints initials.
# Aaron Bolyard
# 2018-04-10
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

def printCircleReverse_ADB(atuin_ADB, radius_ADB, angle_ADB):
    circleSegmentLength_ADB = radius_ADB * math.pi / CIRCLE_QUALITY
    for i in range(0, CIRCLE_QUALITY):
        partialAngle_ADB = angle_ADB / CIRCLE_QUALITY
        atuin_ADB.left(partialAngle_ADB)
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

def printC_ADB(atuin_ADB, size_ADB):
    # Orient C
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB * (3 / 4))
    atuin_ADB.down()
    atuin_ADB.right(90 + 45)

    # Circle
    printCircle_ADB(atuin_ADB, size_ADB * 0.9, 250)

def printD_ADB(atuin_ADB, size_ADB):
    # Side of D
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    # Top of D
    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB / 4)

    # Curve
    printCircle_ADB(atuin_ADB, (size_ADB * 1.25) / 2, 180)

def printE_ADB(atuin_ADB, size_ADB):
    # Move over a little
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB * (3 / 4))
    atuin_ADB.down()

    atuin_ADB.right(90 + 45 / 2)

    # Like B, but flipped
    printCircle_ADB(atuin_ADB, size_ADB / 2, 220)
    atuin_ADB.left(90 + 45)
    printCircle_ADB(atuin_ADB, size_ADB / 2, 220)

def printF_ADB(atuin_ADB, size_ADB):
    # Left span of F
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    # Top span of F
    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * (3 / 4))

    # Move to bottom span of F
    atuin_ADB.up()
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * (3 / 4))
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 2)
    atuin_ADB.left(90)
    atuin_ADB.down()
    atuin_ADB.forward(size_ADB / 2)

def printG_ADB(atuin_ADB, size_ADB):
    # Serif
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * (1 / 8))
    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * (2 / 4))
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * (1 / 8))
    atuin_ADB.right(90)
    atuin_ADB.down()
    atuin_ADB.forward(size_ADB * (1 / 4))
    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * (1 / 4))
    atuin_ADB.right(45)

    # Circle
    printCircle_ADB(atuin_ADB, size_ADB * 0.9, 250)

def printH_ADB(atuin_ADB, size_ADB):
    # Left span
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * 1.25 / 2)
    atuin_ADB.left(90)

    # Middle span
    atuin_ADB.forward(size_ADB / 2)

    # Right span
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 / 2)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * 1.25)

def printI_ADB(atuin_ADB, size_ADB):
    # Middle span
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB / 2)
    atuin_ADB.down()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    # Top span
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 4)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB / 2)

    # Move to bottom span
    atuin_ADB.left(180)
    atuin_ADB.forward(size_ADB / 4)
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    # Bottom span
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 4)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB / 2)

def printJ_ADB(atuin_ADB, size_ADB):
    # Middle span
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 2)
    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * 1.25 * (1 / 4))
    atuin_ADB.down()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 * (2 / 4))

    # Move to bottom span
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * 1.25 * (2 / 4))

    # Circle thingy at bottom of J
    printCircle_ADB(atuin_ADB, size_ADB / 4, 90)

def printK_ADB(atuin_ADB, size_ADB):
    # Left span of K
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * 1.25 / 2)
    atuin_ADB.left(90)

    # Top diagonal of K
    atuin_ADB.left(45)
    atuin_ADB.forward(size_ADB * (3 / 4))
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * (3 / 4))

    # Bottom diagonal of K
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * (3 / 4))

def printL_ADB(atuin_ADB, size_ADB):
    # Left span of L
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB * 1.25)

    # Bottom span of L
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 2)

def printM_ADB(atuin_ADB, size_ADB):
    # Left span of M
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    # Left-middle span of M
    atuin_ADB.right(90 + 45)
    atuin_ADB.forward(size_ADB / 2)

    # Right-middle span of M
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 2)

    # Right span of M
    atuin_ADB.right(90 + 45)
    atuin_ADB.forward(size_ADB * 1.25)

def printN_ADB(atuin_ADB, size_ADB):
    # Left span of N
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    # Middle span of N
    atuin_ADB.right(90 + 45 + 45 / 2)
    atuin_ADB.forward(size_ADB * math.sqrt(2))

    # Middle span of N
    atuin_ADB.left(90 + 45 + 45 / 2)
    atuin_ADB.forward(size_ADB * 1.25)

def printO_ADB(atuin_ADB, size_ADB):
    # More like an 0
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 / 4)
    atuin_ADB.down()
    atuin_ADB.forward(size_ADB * 1.25 / 2)

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)

    atuin_ADB.forward(size_ADB * 1.25 / 2)

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)

def printP_ADB(atuin_ADB, size_ADB):
    # Left span of P
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB / 4)

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)
    atuin_ADB.forward(size_ADB / 4)

def printQ_ADB(atuin_ADB, size_ADB):
    # More like an 0
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 / 4)
    atuin_ADB.down()
    atuin_ADB.forward(size_ADB * 1.25 / 2)

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)

    atuin_ADB.forward(size_ADB * 1.25 / 2)

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)

    atuin_ADB.right(90)
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB * 3 / 8)
    atuin_ADB.down()

    atuin_ADB.right(45)
    atuin_ADB.forward(size_ADB / 2)

def printR_ADB(atuin_ADB, size_ADB):
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB / 4)

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)
    atuin_ADB.forward(size_ADB / 4)

    atuin_ADB.left(90 + 45)
    atuin_ADB.forward(size_ADB * (3 / 4))

def printS_ADB(atuin_ADB, size_ADB):
    # It's reversed but I don't care.

    # Move over a little
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB * (3 / 4))
    atuin_ADB.down()

    atuin_ADB.right(90 + 45 / 2)

    # Like B, but flipped
    printCircle_ADB(atuin_ADB, size_ADB / 2, 220)

    atuin_ADB.right(45)
    printCircleReverse_ADB(atuin_ADB, size_ADB / 2, 220)

def printT_ADB(atuin_ADB, size_ADB):
    # Like an I without bottom span.
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB / 2)
    atuin_ADB.down()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)

    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB / 4)
    atuin_ADB.right(180)
    atuin_ADB.forward(size_ADB / 2)

def printU_ADB(atuin_ADB, size_ADB):
    # Like an O but without the top.
    # More like an 0
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 / 4)
    atuin_ADB.down()
    atuin_ADB.forward(size_ADB * 1.25 * (3 / 4))

    atuin_ADB.up()
    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * 3 / 8 * 2)
    atuin_ADB.down()

    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * 1.25 * (3 / 4))

    printCircle_ADB(atuin_ADB, size_ADB * 3 / 8, 180)

def printV_ADB(atuin_ADB, size_ADB):
    # It's a little too wide but I don't care.
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.down()

    atuin_ADB.right(90 + 45 + 45 / 2)
    atuin_ADB.forward(size_ADB * math.sqrt(2))

    atuin_ADB.left(90 + 45)
    atuin_ADB.forward(size_ADB * math.sqrt(2))

def printW_ADB(atuin_ADB, size_ADB):
    # Like W but reversed
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.right(90)
    atuin_ADB.down()

    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * 1.25)

    atuin_ADB.left(90 + 45)
    atuin_ADB.forward(size_ADB / 2)

    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB / 2)

    atuin_ADB.left(90 + 45)
    atuin_ADB.forward(size_ADB * 1.25)

def printX_ADB(atuin_ADB, size_ADB):
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.down()

    atuin_ADB.right(90 + 45 + 45 / 2)
    atuin_ADB.forward(size_ADB * math.sqrt(2))

    atuin_ADB.up()
    atuin_ADB.left(90 + 45 + 45 / 2)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.down()

    atuin_ADB.left(90 + 45 + 45 / 2)
    atuin_ADB.forward(size_ADB * math.sqrt(2))

def printY_ADB(atuin_ADB, size_ADB):
    # Middle span
    atuin_ADB.up()
    atuin_ADB.forward(size_ADB / 2)
    atuin_ADB.down()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 * (3 / 4))

    # Left span
    atuin_ADB.left(45)
    atuin_ADB.forward(size_ADB * 1.25 / 4 * math.sqrt(2))

    # Recenter
    atuin_ADB.left(180)
    atuin_ADB.forward(size_ADB * 1.25 / 4 * math.sqrt(2))

    # Right span
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25 / 4 * math.sqrt(2))

def printZ_ADB(atuin_ADB, size_ADB):
    atuin_ADB.up()
    atuin_ADB.left(90)
    atuin_ADB.forward(size_ADB * 1.25)
    atuin_ADB.down()

    atuin_ADB.right(90)
    atuin_ADB.forward(size_ADB * (3 / 4))

    atuin_ADB.right(90 + 45 - 45 / 2)
    atuin_ADB.forward(size_ADB * math.sqrt(2))

    atuin_ADB.left(90 + 45 - 45 / 2)
    atuin_ADB.forward(size_ADB * (2 / 4))

LETTERS = {
    'A': printA_ADB,
    'B': printB_ADB,
    'C': printC_ADB,
    'D': printD_ADB,
    'E': printE_ADB,
    'F': printF_ADB,
    'G': printG_ADB,
    'H': printH_ADB,
    'I': printI_ADB,
    'J': printJ_ADB,
    'K': printK_ADB,
    'L': printL_ADB,
    'M': printM_ADB,
    'N': printN_ADB,
    'O': printO_ADB,
    'P': printP_ADB,
    'Q': printQ_ADB,
    'R': printR_ADB,
    'S': printS_ADB,
    'T': printT_ADB,
    'U': printU_ADB,
    'V': printV_ADB,
    'W': printW_ADB,
    'X': printX_ADB,
    'Y': printY_ADB,
    'Z': printZ_ADB
}

def main_ADB():
    name_ADB = input("What are your initials?").upper()

    window_ADB = turtle.Screen()
    atuin_ADB = turtle.Turtle()

    atuin_ADB.pensize(20)
    atuin_ADB.pencolor("grey")

    x = -LETTER_SPAN_SIZE * 3
    for letter in name_ADB:
        func = LETTERS.get(letter)
        if func != None:
            resetPen_ADB(atuin_ADB, x, 0)
            func(atuin_ADB, LETTER_SPAN_SIZE)
            x += LETTER_SPAN_SIZE

    window_ADB.mainloop()

main_ADB()
