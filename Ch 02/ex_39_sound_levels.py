"""
Determine decibels to noise
"""

# Get Input
sound_level = int(input("Enter sound level(in decibels): "))
noise = ""

# Compute
if sound_level == 130:
    noise = "of a Jackhammer"
elif sound_level == 106:
    noise = "of a Gas lawnmover"
elif sound_level == 70:
    noise = "of an Alarm clock"
elif sound_level == 40:
    noise = "of a Quiet room"
elif sound_level > 40 and sound_level < 70:
    noise = "between a Quiet room and an Alarm clock"
elif sound_level > 70 and sound_level < 106:
    noise = "between an Alarm clock and a Gas lawnmover"
elif sound_level > 106 and sound_level < 130:
    noise = "between a Gas lawnmover and a Jackhammer"
elif sound_level > 130:
    noise = "too loud"
elif sound_level < 130:
    noise = "too low"

# Display
print(f"The noise from {sound_level} db is {noise}")