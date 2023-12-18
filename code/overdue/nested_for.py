"""
use nested for loop to calculate x^1, x^2, x^3, x^4.
"""

for x in range(1, 5):
    for i in range(1, 5):
        print(f"{x}^{i}:", x**i)
