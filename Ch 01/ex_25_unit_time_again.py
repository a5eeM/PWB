"""
Compute Days:Hours:Minutes:Seconds from seconds
"""
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Get Input
num_seconds = int(input("Enter number of seconds: "))

# Compute
days = num_seconds // SECONDS_PER_DAY
hours = (num_seconds % SECONDS_PER_DAY) // SECONDS_PER_HOUR
minutes = (num_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
seconds = num_seconds % SECONDS_PER_MINUTE

# Display
print(f"{num_seconds} seconds are {days}:{hours:02d}:{minutes:02d}:{seconds:02d}")
