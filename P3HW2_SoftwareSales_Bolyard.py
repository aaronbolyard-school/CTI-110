# P3HW2
# - Calculates the price of buying software after a bulk discount.
# Aaron Bolyard
# 2018-03-20

## Constants.
# Price of the software package, in dollars.
PACKAGE_PRICE  = 99

# Discounts at various thresholds, as a percent.
DISCOUNT_A_ADB = 10
DISCOUNT_B_ADB = 20
DISCOUNT_C_ADB = 30
DISCOUNT_D_ADB = 40
## End constants.

def main_ADB():
    # Local variables.
    discountRate_ADB            = 0.0 # The computed discount rate, as a percent.
    quantity_ADB                = 0.0 # User-provided quantity of software licenses.
    totalPrice_ADB              = 0.0 # Total price of licenses before discount.
    totalPriceAfterDiscount_ADB = 0.0 # Total price of licenses after discount.

    # Get the quantity of licenses.
    quantity_ADB = float(input("Enter how many Widget Software licenses are you buying: "))

    # Compute discounts per requirements.
    if quantity_ADB >= 100:
        discountRate_ADB = DISCOUNT_D_ADB
    elif quantity_ADB >= 50:
        discountRate_ADB = DISCOUNT_C_ADB
    elif quantity_ADB >= 20:
        discountRate_ADB = DISCOUNT_B_ADB
    elif quantity_ADB >= 10:
        discountRate_ADB = DISCOUNT_A_ADB
    else:
        # There is no discount for purchases under 10.
        discountRate_ADB = 0.0

    # Compute the price, before and after discount.
    totalPrice_ADB = (PACKAGE_PRICE * quantity_ADB)
    totalPriceAfterDiscount_ADB = totalPrice_ADB * ((100 - discountRate_ADB) / 100)

    # Display results.
    print("The total price before discounts is ${0:.02f}.".format(totalPrice_ADB))
    print("Your price after discounts is ${0:.02f}.".format(totalPriceAfterDiscount_ADB))
    print("Your discount was {0:.02f}%.".format(discountRate_ADB))
    print("You saved ${0:0.02f}.".format(totalPrice_ADB - totalPriceAfterDiscount_ADB))

# Run a few times.
for i in range(1, 6):
    main_ADB()
