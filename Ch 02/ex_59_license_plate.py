"""
Determine whether a License plate is valid or not
"""

# Get Input
l_plate = input("Enter license plate string: ")
length = len(l_plate)
valid_older = False
valid_newer = False

# Compute
if length == 6 or length == 7:
    if length == 6:
        if l_plate[0].isalpha() and l_plate[1].isalpha() \
        and l_plate[2].isalpha() and l_plate[3].isdigit() and l_plate[4]\
        .isdigit() and l_plate[5].isdigit():
            valid_older = True
    else:
        if l_plate[0].isdigit() and l_plate[1].isdigit() and l_plate[2]\
        .isdigit() and l_plate[3].isdigit() and l_plate[4].isalpha() and \
        l_plate[5].isalpha() and l_plate[6].isalpha():
            valid_newer = True
else:
    valid_newer = False
    valid_older = False

# Display
if valid_older:
    print(f"{l_plate} is valid for older style license plates!")
if valid_newer:
    print(f"{l_plate} is valid for newer style license plates!")
elif not valid_older and not valid_newer:
    print(f"{l_plate} is an invalid license plate!")
