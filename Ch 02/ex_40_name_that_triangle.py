"""
Determine type of a triangle after reading its sides
"""

# Get Input
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

type = ""

# Compute
if side1 == side2 and side2 == side3:
    type = "Equilateral"
elif side1 == side2 or side2 == side3 or side3 == side1:
    type = "Isosceles"
else:
    type = "Scalene"

# Display
print(f"{type} triangle.")
