# CTI-110
# P3LAB:
#  - Fixed grade scoring program.
# Aaron Bolyard
# 2018-03-08
#

def main():
  # This program takes a number grade and outputs a letter grade.

  # System uses 10-point grading scale
  A_SCORE = 90
  B_SCORE = 80
  C_SCORE = 70
  D_SCORE = 60

  score = int(input('Enter grade: '))

  if score >= A_SCORE:
    print('Your grade is: A')
  elif score >= B_SCORE:
    print('Your grade is: B')
  elif score >= C_SCORE:
    print('Your grade is: C')
  elif score >= D_SCORE:
    print('Your grade is: D')
  else:
    print('Your grade is: F')

# Program start.
# There's 5 possible grades.
for i in range(0, 5):
  main()
