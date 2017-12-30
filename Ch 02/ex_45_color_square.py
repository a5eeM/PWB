"""
Determine the color of the square in a chess board
"""

# Get Input
position = input("Enter position: ")
color = ""

# Compute
position_coloumn = position[0]
position_row = int(position[1])

if position_coloumn == "a" or position_coloumn == "c" \
or position_coloumn == "e" or position_coloumn == "g":
    color_start = "black"
else:
    color_start = "white"

if position_row % 2 == 0 and color_start == "black":
    color = "white"
elif position_row % 2 != 0 and color_start == "black":
    color = "black"
elif position_row % 2 == 0 and color_start == "white":
    color = "black"
elif position_row % 2 != 0 and color_start == "white": # a simple 'else:' would suffice also 
    color = "white"

# Display
print(f"{position}'s color is {color}")
