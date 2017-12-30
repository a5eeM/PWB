"""
Simulate a spin of roulette wheel
"""
import random

red_space = False
green_space = False
black_space = False
pay_even = False
pay_odd = False
one_to_eighteen = False
nineteen_to_thirty_six = False

# Generate random input
spin = random.randint(0, 37)

# Compute
if spin == 1 or spin == 3 or spin == 5 or spin == 7 or spin ==  9 or spin == 12 \
or spin == 14 or spin == 16 or spin == 18 or spin == 19 or spin == 21 or \
spin == 23 or spin == 25 or spin == 27 or spin == 30 or spin == 32 or \
spin == 34 or spin == 36:
    red_space = True
elif spin == 0 or spin == 37:
    green_space = True
else:
    black_space = True

if spin >=1 and spin <= 36:
    if spin % 2 == 0:
        pay_even = True
    else:
        pay_odd = True

# Determine lower vs upper payout
if spin >= 1 and spin <= 36:
    if spin >= 1 and spin <= 18:
        one_to_eighteen = True
    elif spin >= 19 and spin <= 36:
        nineteen_to_thirty_six = True

# Display
if green_space:
    if spin == 37:
        print(f"The spin resulted in 00...")
        print("Pay 00")
    else:
        print(f"The spin resulted in {spin}...")
        print(f"Pay {spin}")
print(f"The spin resulted in {spin}...")
if red_space:
    print("Pay Red")
elif black_space:
    print("Pay Black")
if pay_even:
    print("Pay Even")
elif pay_odd:
    print("Pay Odd")
if one_to_eighteen:
    print("Pay 1 to 18")
elif nineteen_to_thirty_six:
    print("Pay 19 to 36")
