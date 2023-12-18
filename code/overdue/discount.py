"""
create branches to calculate discounted price given different inputs.
"""

items = {
    "macbook": 35000,
    "iphone": 28000,
    "ipad": 38000,
    "mac mini": 42000,
}

print("items to sell:")
for item, price in items.items():
    print(item, ":", price)
print("-" * 10)

to_buy = input("what do you want to buy? ").lower()

if items[to_buy] > 32000:
    print(items[to_buy] * 0.8)
elif items[to_buy] > 25000:
    print(items[to_buy] * 0.9)
else:
    print(items[to_buy] - 500)
