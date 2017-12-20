"""
Compute height in centimeters
"""

FOOT_INCH = 12
INCH_CM = 2.54

print("Enter your height in feets and inches:")

# Get Input
feet = int(input("feet: "))
inches = float(input("inches: "))

# Compute
height_cm = INCH_CM * ((feet * FOOT_INCH) + inches)

# Display
print(f"Your height {feet:.0f}ft {inches:.02f}in is {height_cm:.02f}cm")
