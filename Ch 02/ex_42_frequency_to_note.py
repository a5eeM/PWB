"""
Frequency to Note
"""

# Get Input
frequency = float(input("Enter frequency(in Hz): "))
threshold = 1

# Compute
if frequency >= 261.63 - threshold and frequency <= 261.63 + threshold:
    note = "C4"
elif frequency >= 293.66 - threshold and frequency <= 293.66 + threshold:
    note = "D4"
elif frequency >= 329.63 - threshold and frequency <= 329.63 + threshold:
    note = "E4"
elif frequency >= 349.23 - threshold and frequency <= 349.23 + threshold:
    note = "F4"
elif frequency >= 392.00 - threshold and frequency <= 392.00 + threshold:
    note = "G4"
elif frequency >= 440.00 - threshold and frequency <= 440.00 + threshold:
    note = "A4"
elif frequency >= 493.88 - threshold and frequency <= 493.88 + threshold:
    note = "B4"
else:
    note = ""

# Display
if note:
    print(f"{frequency} belongs to {note} note.")
else:
    print("Frequency does not correspond to a known note!!")
