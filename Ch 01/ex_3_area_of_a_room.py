"""
Area of a room
"""
print("Enter the width & length of the room(in meters)")
# Read input
width = float(input("width(m): "))
length = float(input("length(m): "))

# Compute area
area = length * width

# Display
print("Area of the room is {} square meters.".format(area))
