"""
Determine grade from grade points
"""

# Get Input
grade_points = float(input("Enter grade points: "))
grade_letter = ""

# Compute
if grade_points >= 4.0:
    grade_letter = "A+"
elif grade_points >= 3.7 and grade_points < 4.0:
    grade_letter = "A-"
elif grade_points >= 3.3 and grade_points < 3.7:
    grade_letter = "B+"
elif grade_points >= 3.0 and grade_points < 3.3:
    grade_letter = "B"
elif grade_points >= 2.7 and grade_points < 3.0:
    grade_letter = "B-"
elif grade_points >= 2.3 and grade_points < 2.7:
    grade_letter = "C+"
elif grade_points >= 2.0 and grade_points < 2.3:
    grade_letter = "C"
elif grade_points >= 1.7 and grade_points < 2.0:
    grade_letter = "C-"
elif grade_points >= 1.3 and grade_points < 1.7:
    grade_letter = "D+"
elif grade_points >= 1.0 and grade_points < 1.3:
    grade_letter = "D"
else:
    grade_letter = "F"

# Display
print(f"{grade_points} grade points converts to {grade_letter} grade!")