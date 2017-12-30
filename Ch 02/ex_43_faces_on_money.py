"""
Determine name of individiual from denomination of banknote
"""

# Get Input
denomination = int(input("Enter denomination: "))
name = ""

# Compute
if denomination == 1:
    name = "George Washington"
elif denomination == 2:
    name = "Thomas Jefferson"
elif denomination == 5:
    name = "Abraham Lincoln"
elif denomination == 10:
    name = "Alexander Hamilton"
elif denomination == 20:
    name = "Andrew Jackson"
elif denomination == 50:
    name = "Ulysses S. Grant"
elif denomination == 100:
    name = "Benjamin Franklin"
else:
    name = ""

# Display
if name:
    print(f"${denomination} banknote has an image of {name}")
else:
    print("No such note exists!")