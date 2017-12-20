"""
Convert celsius to fahrenheit and kelvin
"""

# Get Input
celsius = float(input("Enter temperature(in celsius): "))

# Compute
temp_in_kelvin = celsius + 273.15
temp_in_fahrenheit = (9/5 * celsius) + 32

# Display
print(f"{celsius:.02f} degree celsius is {temp_in_kelvin:.02f} kelvins or \
{temp_in_fahrenheit:.02f} degree fahrenheit.")