"""
Simple Arithmetic
"""
from math import log10

print("Enter two integers")

# Get Input
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Compute
sm = a + b
diff = a - b
product = a * b
quotient = a / b
remainder = a % b
log_a = log10(a)
a_raise_b = a ** b

# Display
print(f"Sum: {sm}\n" +
      f"Difference: {diff}\n" +
      f"Product: {product}\n" +
      f"Quotient: {quotient:.0f}\n" +
      f"Remainder: {remainder}\n" +
      f"log a: {log_a:.2f}\n" +
      f"a^b: {a_raise_b}")
