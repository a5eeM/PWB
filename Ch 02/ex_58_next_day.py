"""
Determine the immeditate successor from a date given as input
"""

# Get Input
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

is_leap = False
final_day = day
final_month = month
final_year = year
leap_day_feb_mumbo_jumbo = True # prevents user from putting 29 as a day for month 2 when year isn't a leap year.

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = True
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

# Jan, March, May, July, August, October
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8\
or month == 10:
    if day >= 1 and day < 31:
        final_day = day + 1
    elif day == 31:
        final_month = month + 1
        final_day = 1
# February, take leap year into account
if month == 2:
    if is_leap:
        if day >= 1 and day < 29:
            final_day = day + 1
        elif day == 29:
            final_month = month + 1
            final_day = 1
    else:
        if day >= 1 and day < 28:
            final_day = day + 1
        elif day == 28:
            final_month = month + 1
            final_day = 1
        elif day == 29:
            leap_day_feb_mumbo_jumbo = False
# April, June, September, November
if month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day < 30:
        final_day = day + 1
    elif day == 30:
        final_month = month + 1
        final_day = 1
# December, new year
if month == 12:
    if day >= 1 and day < 31:
        final_day = day + 1
    elif day == 31:
        final_year = year + 1
        final_month = 1
        final_day = 1

# Display
if leap_day_feb_mumbo_jumbo:
    print(f"{year}-{month}-{day}: Next day is {final_year}-{final_month:02}-"\
f"{final_day:02}")
else:
    print("Invalid! Not a Leap Year!")
