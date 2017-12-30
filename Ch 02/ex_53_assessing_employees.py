"""
Determine employee performance
"""

# Get Input
rating = float(input("Enter rating: "))
performance = ""

# Compute
if rating >= 0.6:
    performance = "Meritorious"
    raise_amount = 2400 * rating
elif rating == 0.4:
    performance = "Acceptable"
    raise_amount = 2400 * 0.4
elif rating == 0.0:
    performance = "Unacceptable"
    raise_amount = 0
else:
    performance = ""

# Display
if performance:
    print(f"{rating} rating corresponds to {performance} performance \
with a raise of ${raise_amount:.2f}")
else:
    print("Invalid rating! Please try again!")
