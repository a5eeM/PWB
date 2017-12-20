"""
Compute seconds
"""
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Get Input
days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

# Compute
num_sec = (days * SECONDS_PER_DAY) + (hours * SECONDS_PER_HOUR)
num_sec += (minutes * SECONDS_PER_MINUTE) + seconds

# Display
print(f"NUmber of seconds in {days} days, {hours} hours, {minutes} minutes \
and {seconds} seconds are {num_sec} seconds")
