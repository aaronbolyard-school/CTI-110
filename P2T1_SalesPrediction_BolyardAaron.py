# P2T1
# Sales prediction
# Aaron Bolyard
# 2018-02-15

def read_number(prompt):
    string_value = input(prompt)
    try:
        number_value = float(string_value)
        if number_value <= 0:
            print("Bad input. Please enter a positive value.")
            return read_number(prompt)

        return number_value
    except:
        print("Bad input. Please enter a number.")
        return read_number(prompt)

total_sales = read_number("Enter total sales: ")
estimated_profit = total_sales * 0.23

print("Estimated profit: ${0:,.2f}".format(estimated_profit))
