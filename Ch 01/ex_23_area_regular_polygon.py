"""
Compute area of a regular Polygon
"""

from math import pi, tan

# Get Input
number_of_sides = int(input("Enter number of sides: "))
length_of_side = float(input("Enter length of a side: "))

# Compute
area = (number_of_sides * length_of_side**2) / (4 * tan(pi / number_of_sides))

# Display
print(f"Area of the regular polygon with {number_of_sides} sides and \
length of each side {length_of_side:.02f} is {area:.02f}")
