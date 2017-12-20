"""
Tax and Tip
"""

TAX_RATE = 0.05
TIP_RATE = 0.18

# Read cost
meal_cost = float(input("enter the cost of the meal($): "))

# Compute
tip_amount = meal_cost * TIP_RATE
tax_amount = meal_cost * TAX_RATE
grand_amount = meal_cost + tax_amount + tip_amount

# Display
print("Tax amount: ${:.2f}\n".format(tax_amount) +
      "Tip amount: ${:.2f}\n".format(tip_amount) +
      "Grand amount: ${:.2f}".format(grand_amount))

# print("Tip amount: $%.2f\nTax Amount: $%.2f\nGrand amount: $%.2f" % \
#       (tip_amount, tax_amount, grand_amount))
