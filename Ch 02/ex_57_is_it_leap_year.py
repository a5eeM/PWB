"""
Determine whether a year is a leap year
"""

# Get Input
year = int(input("Enter a year: "))
is_leap = False

# Compute
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = True
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

# Display
if is_leap:
    print(f"{year} is a leap year!!")
else:
    print(f"{year} is not a leap year!")
