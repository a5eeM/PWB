"""
Compute volume of a cylinder
"""
from math import pi

# Get Input
radius = float(input("Enter radius: "))
height = float(input("Enter heigh: "))

# Compute
volume = pi * radius**2 * height

# Display
print(f"Volume of the cylinder is {volume:.02f}")
