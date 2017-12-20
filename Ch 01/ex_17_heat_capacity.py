"""
Compute enery
"""

HEAT_CAPACITY_WATER = 4.186
COST_PER_KW_HOUR = 0.089
JOULE_TO_KWH = 2.7778e-7

# Get Input
mass = float(input("Enter the amount of water: "))
temp_change = float(input("Enter the temperature change: "))

# Compute
energy_kw = mass * HEAT_CAPACITY_WATER * temp_change * JOULE_TO_KWH
cost = energy_kw * COST_PER_KW_HOUR

# Display
print(f"Cost of boiling {mass:.0f} gram water for a cup of coffe \
is ${cost:.05f}")
