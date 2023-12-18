"""
利用 Python 運算子，分別將 萬，千，百，十，個位數 顯示出來
"""

number = int(input("請輸入一組數字: "))

print(number // 10000)
print((number % 10000) // 1000)
print((number % 1000) // 100)
print((number % 100) // 10)
print(number % 10)
