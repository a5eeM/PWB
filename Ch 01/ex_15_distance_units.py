"""
Compute distance in inches, yards and miles
"""
INCHES_PER_FOOT = 12
YARDS_PER_FOOT = 0.33
MILES_PER_FOOT = 0.000189394

print("Enter distance in feet:")

# Get Input
feet = float(input("feet: "))

# Compute
distance_inches = feet * INCHES_PER_FOOT
distance_yards = feet * YARDS_PER_FOOT
distance_miles = feet * MILES_PER_FOOT

# Display
print(f"You travelled a distance of {feet:.0f} feet, or {distance_inches:.0f} inches,\
or {distance_yards:.02f} yards, or {distance_miles:.02f} miles.")
