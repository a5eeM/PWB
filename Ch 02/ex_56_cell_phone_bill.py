"""
Determine phone bill from number of minutes and texts
"""

BASE_CHARGE = 15.00
ADDN_AIR_TIME_MINUTE = 0.25
ADDN_TEXT = 0.15
NINE_11 = 0.44
TAX_RATE = 0.05

# Get Input
num_minutes = int(input("Enter number of minutes: "))
num_text = int(input("Enter number of texts: "))
bill = None

# Compute
if num_minutes > 50:
    additonal_minutes = num_minutes - 50
    additional_minute_charge = additonal_minutes * ADDN_AIR_TIME_MINUTE
else:
    additonal_minutes = 0
    additional_minute_charge = 0.0
if num_text > 50:
    additonal_texts = num_text - 50
    additional_text_charge = additonal_texts * ADDN_TEXT
else:
    additonal_texts = 0
    additional_text_charge = 0.0

bill = BASE_CHARGE + additional_minute_charge + additional_text_charge \
+ NINE_11
tax = TAX_RATE * bill
total_bill = bill + tax

# Display
print("\nBill:")
print(f" Base Charge: ${BASE_CHARGE:.2f}")
print(f" Additional Minutes Charge: {additonal_minutes} *"\
f" {ADDN_AIR_TIME_MINUTE} = ${additional_minute_charge:.2f}")
print(f" Additional Text Charge: {additonal_texts} *"\
f" {ADDN_TEXT} = ${additional_text_charge:.2f}")
print(f" 911 fee: ${NINE_11:.2f}")
print(f" TAX: ${tax:.2f}")
print(f" Total Bill: ${total_bill:.2f}")
