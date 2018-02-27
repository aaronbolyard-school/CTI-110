# CTI-110
# P2HW2:
#  - Calculates the tip, tax, and total of an order.
#  - Builds a receipt from a database of items.
#  - Handles input validation.
# Aaron Bolyard
# 2018-02-27
#

## Data structures

# Structure of an Item.
#
# An item is something a person can buy.
class Item:
    primaryKey = 0
    name = "none"
    price = 0.00

    def __init__(self, primaryKey, name, price):
        self.primaryKey = primaryKey
        self.name = name
        self.price = price

# Maps integer primary keys to items.
class ItemDatabase:
    items = {}

    # Constructs an item database from a CSV-encoded string.
    def __init__(self, csvString):
        # Split the CSV string into lines
        lines = csvString.splitlines(False)

        # Iterate over the lines and parse.
        for line in lines:
            row = line.split(',')

            itemPrimaryKey = int(row[0].strip())
            itemName = row[1].strip()
            itemPrice = float(row[2].strip())

            self.items[itemPrimaryKey] = Item(itemPrimaryKey, itemName, itemPrice)
        
    # Gets the item with the matching primary key.
    #
    # Returns None if the item was not found.
    def getItem(self, primaryKey):
        return self.items.get(int(primaryKey), None)
        
    # Prints the item primary key and item name.
    def printItems(self):
        print("KEY", "PRICE", "ITEM", sep="\t")
        for _, item in self.items.items():
            print(item.primaryKey, format(item.price, ".02f"), item.name, sep="\t")

# End data structures

# Displays 'prompt' and reads a number.
#
# Correctly handles erroneous input.
#
# Returns the number.
def readNumber(prompt):
    string_value = input(prompt)
    try:
        number_value = float(string_value)

        # Ensure the number is greater than or equal to zero. If not, try again.
        if number_value < 0:
            print("Bad input. Please enter a positive or zero value.")
            return readNumber(prompt)

        return number_value
    except:
        # The user entered a non-numerical value. Try again.
        print("Bad input. Please enter a number.")
        return readNumber(prompt)

# Builds a receipt from user input.
def buildReceipt():
    receipt = []

    ITEM_DATABASE.printItems()
    print("Add items. Enter 0 to quit.")
    primaryKey = readNumber("Item:")
    while primaryKey != 0:
        item = ITEM_DATABASE.getItem(primaryKey)
        if item == None:
            print("Item {0:.0f} not found.".format(primaryKey))
        else:
            print("Added {0} (${1:2.02f})".format(item.name, item.price))
            receipt.append(item)

        primaryKey = readNumber("Item:")

    return receipt

# Calculates the price of the receipt.
def getReceiptTotal(receipt):
    price = 0.0

    for item in receipt:
        price += item.price

    return price

# Nicely prints the receipt.
def printReceipt(receipt):
    for item in receipt:
        print("- {0}: ${1:2.02f}".format(item.name, item.price))

## Constants

ITEM_CSV = '''101, Hamburger Jr, 1.49
102, Cheeseburger, 2.49
103, Baconburger, 3.29
201, 6 pc Chicken nuggets, 1.49
202, 12 pc Chicken nuggets, 2.49
301, Small fries, 0.99
302, Medium fries, 1.29
303, Large fries, 2.29
311, 3 pc Mozzarella sticks, 0.99
312, 6 pc Mozzarella sticks, 1.29
601, Small fountain drink, 0.99
602, Medium fountain drink, 1.29
603, Large fountain drink, 1.49'''

ITEM_DATABASE = ItemDatabase(ITEM_CSV)

# Sales tax, as a percent of the sub-total.
SALES_TAX_RATE = 7

# Tip, as a percent of the sub-total.
TIP_RATE = 18

# Decoration.
#
# In Jhonen Vasquez's comic "I Feel Sick" there's a restaurant that
# changes its name from "Please Eat Here" (paraphrased) to something
# more commanding. I think that's how it goes.
RESTAURANT_NAME = "Eat Here or Die"
RESTAURANT_ADDRESS = "123 Example St, Faketteville, NC 12345"
WAITER_NAME = "Bob Smith"

## End constants

## Variables

receipt         = [] # The receipt, as inputed by the waiter (WAITER_NAME)

orderGrossTotal = 0.0 # Gross total, before tax and tip.
orderSubTotal   = 0.0 # Order sub-total. This is input by the user.
orderTip        = 0.0 # Tip, computed from total and tip percent.
orderTax        = 0.0 # Tax, compute from sales tax and total.
orderNetTotal   = 0.0 # Net total, after tax and tip.

## Program logic.
receipt = buildReceipt()
orderGrossTotal = getReceiptTotal(receipt)

print("Gross total: ${0:.02f}".format(orderGrossTotal))

# Get the order sub-total.
orderSubTotal = readNumber("Enter subtotal: $")

# Calculate the components.
orderTax = orderSubTotal * (SALES_TAX_RATE / 100)
orderTip = orderSubTotal * (TIP_RATE / 100)

# Calculate the net total.
orderNetTotal = orderSubTotal + orderTax + orderTip

# Print receipt!

print()
print("RECEIPT")
print(RESTAURANT_NAME)
print(RESTAURANT_ADDRESS)
print("You were served by {0}".format(WAITER_NAME))
print("---")
printReceipt(receipt)
print("---")
print("Subtotal: ${0:.02f}".format(orderSubTotal))
print("Tip ({1:2.02f}%): ${0:.02f}".format(orderTip, TIP_RATE))
print("Tax ({1:2.02f}%): ${0:.02f}".format(orderTax, SALES_TAX_RATE))
print("Total: ${0:.2f}".format(orderNetTotal))
