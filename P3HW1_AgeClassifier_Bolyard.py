# P3HW1
# - Determines classification of person's age.
# Aaron Bolyard
# 2018-03-20

# Classifies the age of the user. Prints the result
def classifyAge_ADB(age_ADB):
    if age_ADB < 0:
        print("The person is a time traveler.")
    elif age_ADB <= 1:
        print("The person is an infant.")
    elif age_ADB < 13:
        print("The person is a child.")
    elif age_ADB < 20:
        print("The person is a teenager.")
    elif age_ADB < 65:
        print("The person is an adult.")
    elif age_ADB < 100:
        print("The person is a senior citizen.")
    else:
        print("The person is a centenarian.")
        print("If they were in the UK, they would have gotten a letter from the Queen.")
        

# Main program.
def main_ADB():
    # Age of person, in years.
    age_ADB = 0.0

    # Get age of person.
    age_ADB = int(input("Enter the age of the person: "))

    classifyAge_ADB(age_ADB)

for i in range(1, 8):
    main_ADB()
