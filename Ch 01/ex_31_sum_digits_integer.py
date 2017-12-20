"""
display sum of digits of a four digit integer
"""

# Get Input
number = int(input("Enter any 4 digut number: "))

# Compute
n1 = number % 10
number = number // 10
n2 = number % 10
number = number // 10
n3 = number % 10
number = number // 10

# Display
print(f"{number} + {n3} + {n2} + {n1} = {number + n3 + n2 + n1}")
