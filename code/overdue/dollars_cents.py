# 1729 Pennies in Dollars and Cents

pennies = 1729

print(f"given {pennies} pennies, convert it into dollars and cents.")

# // symbol will return only the integer part
dollars = pennies // 100
# % symbol will return only the remainder
cents = pennies % 100

# so that we can have it in dollars and cents
print(f"dollars: {dollars}")
print(f"cents: {cents}")
