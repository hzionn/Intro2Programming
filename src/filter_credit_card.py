"""
credit card validation.
"""

credit_card = "1234-5678-9123"
credit_card = input("your credit card number (e.g. 1234-5678-9123): ")
filtered_credit_card = ""

for character in credit_card:
    if character != " " and character != "-":
        filtered_credit_card += character

print(filtered_credit_card)
