"""
Determine Chinese Zodiac
"""

# Get Input
year = int(input("Enter any year(> 0): "))
zodiac = ""

# Compute
if year % 12 == 0:
    zodiac = "Monkey"
elif year % 12 == 1:
    zodiac = "Rooster"
elif year % 12 == 2:
    zodiac = "Dog"
elif year % 12 == 3:
    zodiac = "Pig"
elif year % 12 == 4:
    zodiac = "Rat"
elif year % 12 == 5:
    zodiac = "Ox"
elif year % 12 == 6:
    zodiac = "Tiger"
elif year % 12 == 7:
    zodiac = "Hare"
elif year % 12 == 8:
    zodiac = "Dragon"
elif year % 12 == 9:
    zodiac = "Snake"
elif year % 12 == 10:
    zodiac = "Horse"
elif year % 12 == 11:
    zodiac = "Sheep"

# Display
print(f"{year} in chinese zodiac is {zodiac}")
