"""
use while loop to calculate the sum of given numbers
"""

input_number = input("請輸入一組數字：")

# init sum
sum = 0

# how many times we need to loop through
length = len(input_number)
i = 0

while i < length:
    sum += int(input_number[i])
    i += 1

print("數字的總和是：", sum)
