"""
Check whether the integer is even or odd.
"""

# Get Input
number = int(input("Enter any integer: "))

# Check
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
