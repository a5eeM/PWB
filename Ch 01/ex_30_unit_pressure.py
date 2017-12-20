"""
Compute pressure in pounds per square inch, millimeters of Hg & atmospheres.
"""

POUND_PER_KPA = 0.145038
MM_PER_KPA = 7.50062
ATM_PER_KPA = 0.00986923

# Get Input
pressure = float(input("Enter pressure(in kilopascals): "))

# Compute
pressure_in_pound = pressure * POUND_PER_KPA
pressure_in_mmhg = pressure * MM_PER_KPA
pressure_in_atm = pressure * ATM_PER_KPA

# Display
print(f"{pressure:.02f} kilopascals is {pressure_in_pound:.02f} pounds \
per square inch, {pressure_in_mmhg:.02f} mm Hg, {pressure_in_atm:.02f} \
atmospheres.")
