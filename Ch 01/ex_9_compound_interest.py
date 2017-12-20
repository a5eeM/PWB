"""
Compute Compound Interest
"""

RATE = 0.04

# Get Input
principle_amount = float(input("enter the amoun to be deposited: "))

# Compute
amount_first = principle_amount * (1 + RATE)
amount_second = principle_amount * (1 + RATE)**2
amount_third = principle_amount * (1 + RATE)**3

# Display
print("Amount:\n\tafter 1 year:  ${:.2f}\n".format(amount_first) +
      "\tafter 2 years: ${:.2f}\n".format(amount_second) +
      "\tafter 3 years: ${:.2f}".format(amount_third))
