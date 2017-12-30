"""
Identifying Vowels & Consonants
"""

# Get input
read_letter = input("Enter a letter: ")

# Compute & Display
if read_letter == "a" or read_letter == "e" or read_letter == "i" \
or read_letter == "o" or read_letter == "u":
    print(f"{read_letter} is a vowel.")
elif read_letter == "y":
    print(f"{read_letter} is sometimes a vowel, sometime sa consonant.")
else:
    print(f"{read_letter} is a consonant.")
