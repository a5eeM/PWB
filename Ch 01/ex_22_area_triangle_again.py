"""
Compute area of triangle when sides are given
"""

from math import sqrt

# Get Input
s1 = float(input("Enter first side: "))
s2 = float(input("Enter second side:  "))
s3 = float(input("Enter third side: "))

# Compute
s = (s1 + s2 + s3) / 2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

# Display
print(f"Area of the triangle is {area:.02f}")
