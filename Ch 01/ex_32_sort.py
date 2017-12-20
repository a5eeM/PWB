"""
Sort 3 integers from smallest to largest
"""

# Get Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Compute
sum = a + b +c
mn = min(a, b, c)
mx = max(a, b, c)
middle = sum - (mn + mx)

# Display
print(f"Sorted numbers are {mn}, {middle}, {mx}")
