"""
Compute Body Mass Index
"""

# Get Input
height = float(input("Enter height(in metres): "))
weight = float(input("Enter weight(in kilograms): "))


# Compute
bmi = weight / (height ** 2)

# Display
print(f"Your BMI is {bmi:.02f}")
