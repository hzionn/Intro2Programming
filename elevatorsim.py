"""
（電梯停靠樓層）
"""

floor = int(input("floor: "))

if floor == 13:
    actualFloor = floor - 1
elif floor == 14:
    actualFloor = floor + 1
else:
    actualFloor = floor

print("The elevator will travel to the actual floor", actualFloor)
