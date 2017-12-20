"""
Compute Wind Chill Index
"""

# Get Input
air_temp = float(input("Enter air temperature(in celsius): "))
wind_speed = float(input("Enter wind speed(in km/h): "))

# Compute
wind_chill_index = 13.12 + (0.6215 * air_temp) - (11.37 * (wind_speed**0.16))
wind_chill_index += (0.3965 * air_temp * (wind_speed**0.16))

# Display
print(f"Wind Chill Index is {wind_chill_index:.02f}")
