"""
Compute amount of gas in moles
"""

IDEAL_GAS_CONST = 8.314

# Get Input
pressure = float(input("Enter pressure(in Pascals): "))
volume = float(input("Enter volume(in litres): "))
temp = float(input("Enter temperature(in celsius): "))
temp_in_kelvin = temp + 273.15

# Compute
amount_of_gas = (pressure * volume) / (IDEAL_GAS_CONST * temp_in_kelvin)

# Display
print(f"Amount of gas is: {amount_of_gas:.02f} moles")