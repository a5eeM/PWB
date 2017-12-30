"""
Determine the name of the shape from sides
"""

# Read Input
num_sides = int(input("Enter number of sides(from 3 - 10): "))
shape = ""

# Compute
if num_sides == 3:
    shape = "Triangle"
elif num_sides == 4:
    shape = "Quadrilateral"
elif num_sides == 5:
    shape = "Pentagon"
elif num_sides == 6:
    shape = "Hexagon"
elif num_sides == 7:
    shape = "Heptagon"
elif num_sides == 8:
    shape = "Octagon"
elif num_sides == 9:
    shape = "Nonagon"
elif num_sides == 10:
    shape = "Decagon"

# Display
if shape == "":
    print(f"{num_sides} size not supported!")
else:
    print(f"{num_sides} sides is a {shape}")
