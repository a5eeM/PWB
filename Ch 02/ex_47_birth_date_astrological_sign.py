"""
Determine zodiac sign from birth date
"""

# Get Input
month = input("Enter month: ")
date = int(input("Enter date: "))
zodiac = ""

# Compute
if (month == "December" and date >= 22) or (month == "January" and date <= 19):
    zodiac = "Capricorn"
elif (month == "January" and date >= 20) or (month == "February" and \
date <= 18):
    zodiac = "Aquarius"
elif (month == "February" and date >= 19) or (month == "March" and date <= 20):
    zodiac = "Pisces"
elif (month == "March" and date >= 21) or (month == "April" and date <= 19):
    zodiac = "Aries"
elif (month == "April" and date >= 20) or (month == "May" and date <= 20):
    zodiac = "Taurus"
elif (month == "May" and date >= 21) or (month == "June" and date <= 20):
    zodiac = "Gemini"
elif (month == "June" and date >= 21) or (month == "July" and date <= 22):
    zodiac = "Cancer"
elif (month == "July" and date >= 23) or (month == "August" and date <= 22):
    zodiac = "Leo"
elif (month == "August" and date >= 23) or (month == "September" and date <= 22):
    zodiac = "Virgo"
elif (month == "Septembet" and date >= 23) or (month == "October" and date <= 22):
    zodiac = "Libra"
elif (month == "October" and date >= 23) or (month == "November" and date <= 21):
    zodiac = "Scorpio"
elif (month == "November" and date >= 22) or (month == "December" and date <= 21):
    zodiac = "Sagittarius"

# Display
print(f"{month} {date} is {zodiac}")


