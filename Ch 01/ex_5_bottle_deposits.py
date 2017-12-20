"""
Bottle Deposits
"""

DEPOSIT_ONE = 0.10
DEPOSIT_ALL_OTHER = 0.25

print("Enter the number of containers of each size")
# Get input
one_litre = int(input("one litre containers: "))
more_than_one = int(input("more than one litre containers: "))

# Compute
refund = (one_litre * DEPOSIT_ONE) + (more_than_one * DEPOSIT_ALL_OTHER)

# Display
print("Refund for returning containers: ${:.2f}".format(refund))
