"""
Compute the area of a circle and volume of a sphere
"""

from math import pi

# Get input
radius = float(input("Enter the radius: "))

# Compute
area_circle = pi * radius**2
volume_sphere = 4/3 * pi * radius**3

# Display
print(f"Area of the circle with radius {radius} is {area_circle:.02f} \
and the Volume of the sphere with radius {radius} is {volume_sphere:.02f}")
