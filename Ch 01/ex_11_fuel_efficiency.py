"""
Convert MPG(miles-per-gallon) to litres-per-hundred-kilometers
"""

# Get Input
mileage = float(input("Enter your milegae in miles-per-gallin(MPG): "))

# Compute
mileage_lphk = 100 / ((mileage * 1.609) / 3.785)

# Display
print(f"Fuel efficiency in Canadian litres-per-hundred-kilometers: \
{mileage_lphk:.2f}")
