"""
check if this is a valid phone number.
"""

phone_number = "(703)321-6753"
phone_number = input("your phone number, e.g. (703)321-6753: ")
pos = 0
valid_count = 0

while len(phone_number) == 13 and pos < len(phone_number):
    if pos == 0 and phone_number[pos] == "(":
        valid_count += 1
    elif pos == 4 and phone_number[pos] == ")":
        valid_count += 1
    elif pos == 8 and phone_number[pos] == "-":
        valid_count += 1
    elif pos not in (0, 4, 8) and phone_number[pos].isdigit():
        valid_count += 1
    pos += 1

if valid_count == len(phone_number):
    print("VALID phone number")
else:
    print("INVALID phone number")

