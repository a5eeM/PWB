"""
Determine earthquake descriptor from Richter Scale reading
"""

# Get Input
reading = float(input("Enter reading: "))
descriptor = ""

# Compute
if reading < 2.0:
    descriptor = "Micro"
elif reading >= 2.0 and reading < 3.0:
    descriptor = "Very minor"
elif reading >= 3.0 and reading < 4.0:
    descriptor = "Minor"
elif reading >= 4.0 and reading < 5.0:
    descriptor = "Light"
elif reading >= 5.0 and reading < 6.0:
    descriptor = "Moderate"
elif reading >= 6.0 and reading < 7.0:
    descriptor = "Strong"
elif reading >= 7.0 and reading < 8.0:
    descriptor = "Major"
elif reading >= 8.0 and reading < 10.0:
    descriptor = "Great"
elif reading >= 10.0:
    descriptor = "Meteoric"

# Display
print(f"Magnitude {reading} earthquake is considered to be a {descriptor} \
earthquake.")
