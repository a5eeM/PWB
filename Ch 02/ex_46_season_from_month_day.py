"""
Determine season from month and day
"""

# Get Input
month = input("Enter month: ")
date = int(input("Enter date: "))
season = ""

# Compute
if (month == "March" and date >= 20) or (month == "June" and date < 21) \
or month == "April" or month == "May":
    season = "Spring"
elif (month == "June" and date >= 21) or (month == "September" and date < 22) \
or month == "July" or month == "August":
    season = "Summer"
elif (month == "September" and date >= 22) or (month == "December" and date \
< 21) or month == "October" or month == "November":
    season = "Fall"
elif (month == "December" and date >= 21) or (month == "March" and date \
< 20) or month == "January" or month == "February":
    season = "Winter"

# Display
print(f"{month} {date} is associated with {season}")
