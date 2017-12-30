"""
Determine name of the electromagnetic radiation from frequency
"""

MICROWAVES = 3 * (10 ** 9)
INFRARED_LIGHT = 3 * (10 ** 12)
VISIBLE_LIGHT = 4.3 * (10 ** 14)
ULTRAVIOLET_LIGHT = 7.5 * (10 ** 14)
X_RAYS = 3 * (10 ** 17)
GAMMA_RAYS = 3 * (10 ** 19)

# Get Input
frequency = float(input("Enter frequency(in Hz): "))
name = ""

# Compute
if frequency < MICROWAVES:
    name = "Radio Waves"
elif frequency < INFRARED_LIGHT:
    name = "Microwaves"
elif frequency < VISIBLE_LIGHT:
    name = "Infrared light"
elif frequency < ULTRAVIOLET_LIGHT:
    name = "Visible light"
elif frequency < X_RAYS:
    name = "Ultraviolet light"
elif frequency < GAMMA_RAYS:
    name = "X-rays"
else:
    name = "Gamma rays"

# Display
print(f"{frequency} Hz corresponds to {name}!")
