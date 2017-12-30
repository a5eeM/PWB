"""
Note to frequency.
"""

# Get Input
note = input("Enter name of a note: ")
note_name = note[0]
note_octave = int(note[1])
frequency = 0

# Compute
if note_name == "C":
    frequency = 261.63
elif note_name == "D":
    frequency = 293.66
elif note_name == "E":
    frequency = 329.63
elif note_name == "F":
    frequency = 349.23
elif note_name == "G":
    frequency = 392.00
elif note_name == "A":
    frequency = 440.00
elif note_name == "B":
    frequency = 493.88

# adjust octave
frequency = frequency / 2 ** (4 - note_octave)

# Display
print(f"{note}'s frequency is {frequency:.2f} Hz")