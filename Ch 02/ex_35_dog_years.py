"""
Human to Dog years conversion
"""
# Get Input
years = int(input("Enter number of years: "))

# Compute
if years <= 2:
    dog_years = 10.5 * years
else:
    years_counts_as_four = years - 2
    dog_years = 10.5 * 2 + (4 * years_counts_as_four)

# Display
print(f"{years} human years are {dog_years:.0f} dog years!!")
