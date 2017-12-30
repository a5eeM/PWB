"""
Determine holday from date
"""

# Get Input
month = input("Enter month: ")
date = int(input("Enter date: "))

holiday = ""

# Compute
if month == "January" and date == 1:
    holiday = "New year's day"
elif month == "July" and date == 1:
    holiday = "Canada day"
elif month == "December" and date == 25:
    holiday = "Christmas day"
else:
    holiday = ""

# Display
if holiday:
    print(f"{month} {date} is {holiday}.")
else:
    print(f"{month} {date} does not correspond to a fixed-date holiday!")
