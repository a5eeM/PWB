"""
Compute roots of quadratic equations
"""

import math

# Get Input
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
num_roots = ""

# Compute
d = (b ** 2) - (4 * a * c)
if d > 0:
    num_roots = 2
elif d < 0:
    num_roots = 0
elif d == 0:
    num_roots = 1

if num_roots == 0:
    roots = ""
elif num_roots == 1:
    roots = -b / (2 * a)
else:
    roots = (-b + math.sqrt(d)) / (2 * a)
    roots_two = (-b - math.sqrt(d)) / (2 * a)

# Display
if num_roots == 0:
    print(f"{num_roots} real roots!")
elif num_roots == 1:
    print(f"{num_roots} real root which is {roots:.2f}")
else:
    print(f"{num_roots} roots which are {roots:.2f}, {roots_two:.2f}")
