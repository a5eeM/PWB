"""
Compute the price of the bread.
"""

COST_OF_BREAD = 3.49
DISCOUNT_RATE = 0.60

# Get Input
number_of_bread = int(input("Enter number of loaves of day old bread: "))

# compute
actual_price = number_of_bread * COST_OF_BREAD
discount = actual_price * DISCOUNT_RATE
day_old_price = actual_price - discount

# Display
print(f"Regular price: ${actual_price:.02f}, \
Discount: ${discount:.02f}, \
Total Price: ${day_old_price:.02f}")
