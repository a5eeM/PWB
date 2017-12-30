"""
Determine grade points from grade
"""

# Get Input
grade_letter = input("Enter grade: ")
grade_points = None
# Compute
if grade_letter == "A+" or grade_letter == "A":
    grade_points = 4.0
elif grade_letter == "A-":
    grade_points = 3.7
elif grade_letter == "B+":
    grade_points = 3.3
elif grade_letter == "B":
    grade_points = 3.0
elif grade_letter == "B-":
    grade_points = 2.7
elif grade_letter == "C+":
    grade_points = 2.3
elif grade_letter == "C":
    grade_points = 2.0
elif grade_letter == "C-":
    grade_points = 1.7
elif grade_letter == "D+":
    grade_points = 1.3
elif grade_letter == "D":
    grade_points = 1.0
elif grade_letter == "F":
    grade_points = 0
else:
    grade_points = "INVALID"

# Display
if grade_points == "INVALID":
    print(f"{grade_letter} corresponds to {grade_points} grade points!")
else:
    print(f"{grade_letter} corresponds to {grade_points} grade points!")
