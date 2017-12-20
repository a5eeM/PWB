"""
Compute area of a field and display the result in acres.
"""
SQMT_PER_ACRE = 4046.86
print("Enter the length and width of the field in meters.")

# Get input
length = float(input("length(m): "))
width = float(input("width(m): "))

# Compute
area_in_acres = length * width / SQMT_PER_ACRE

# Display
print("Area of the field is {:.2f} acres.".format(area_in_acres))
