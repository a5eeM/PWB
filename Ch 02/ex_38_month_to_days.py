"""
Determine number of days from a month
"""

# get input
month = input("Enter month's name: ")
num_days = ""

# Compute
if month == "January" or  month == "March" or month == "May" \
or month == "July" or month == "August" or month == "October" \
or month == "December":
    num_days = 31
elif month == "April" or month == "June" or month == "September" \
or month == "November":
    num_days = 30
elif month == "February":
    num_days = "28 or 29"
else:
    num_days = ""

# Display
if num_days == "":
    print(f"Month name \"{month}\" does not exist.")
else:
    print(f"{month} has {num_days} days.")
