"""
speed in free fall
"""

from math import sqrt

ACC_G = 9.8
INITIAL_VELOCITY = 0


# Get Input
height = float(input("Enter drop height: "))

# Compute
velocity = sqrt(INITIAL_VELOCITY**2 + 2 * ACC_G* height)

# Display
print(f"Velocity when the object hits the ground is {velocity:.02f} \
meters per second")
