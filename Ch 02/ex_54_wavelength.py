"""
Determine color from Wavelength
"""

# Get Input
wavelength = float(input("Enter wavelength(in nm): "))
color = ""

# Compute
if wavelength < 380 or wavelength > 750:
    color = ""
elif wavelength >= 380 and wavelength < 450:
    color = "Violet"
elif wavelength >= 450 and wavelength < 495:
    color = "Blue"
elif wavelength >= 495 and wavelength < 570:
    color = "Green"
elif wavelength >= 570 and wavelength < 590:
    color = "Yellow"
elif wavelength >= 590 and wavelength < 620:
    color = "Orange"
elif wavelength >= 620 and wavelength < 750:
    color = "Red"

# Display
if color:
    print(f"{wavelength} nm corresponds to {color} color!")
else:
    print(f"{wavelength} nm is outside of the visible spectrum.")
