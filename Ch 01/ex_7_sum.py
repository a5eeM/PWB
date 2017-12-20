"""
Sum of the first n positive integers
"""
# Get input
number = int(input("Enter any positive integer: "))

# Calculate
sm = (number * (number + 1)) / 2

# Display
print("Sum of first %d integers is %d." % \
      (number, sm))

print("Sum of first {:d} integers is {:.0f}.".format(
    number, sm))

print("Sum of first", number, "integers is", sm)
