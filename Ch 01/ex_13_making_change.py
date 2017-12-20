"""
Compute the change
"""

PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
LOONIE = 100
TOONIE = 200

# GET Input
change = int(input("Enter the amount in cents: "))

# Compute
toonies = change // TOONIE
loonies = (change % TOONIE) // LOONIE
quarters = (change % LOONIE) // QUARTER
dimes = (change % QUARTER) // DIME
nickels = (change % DIME) // NICKEL
pennies = (change % NICKEL) // PENNY

# Display
print(f"Your {change} cents will be given as {toonies:.0f} toonies,\
 {loonies:.0f} loonies, {quarters:.0f} quarters, {dimes:.0f} dimes, \
 {nickels:.0f} nickels and {pennies:.0f} pennies")
