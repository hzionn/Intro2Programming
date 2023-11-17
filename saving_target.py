"""
以本金、利率來計算共需要多少年才能達到你的目標金額。

* 本金、利率、目標金額自訂
"""

# 初始化
initial_amount = float(input("請輸入本金："))
interest_rate = float(input("請輸入年利率（以百分比表示）：")) / 100
target_amount = float(input("請輸入目標金額："))

# 複製本金到一個新變量，用於計算
current_amount = initial_amount

# 初始化年數
years = 0

# 使用 while 迴圈計算年數
while current_amount < target_amount:
    # 增加利息
    current_amount += current_amount * interest_rate
    # 增加年數計數
    years += 1

# 輸出結果
print(f"需要 {years} 年，本金 {initial_amount} 元可以增長到 {target_amount} 元。")

