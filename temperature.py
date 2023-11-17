"""
攝氏溫度與華氏溫度的轉換
"""

# 設定攝氏溫度為 42 度
celsius = 42

# 轉換公式：F = C * 9/5 + 32
fahrenheit = celsius * 9/5 + 32

celsius_formatted = f"{celsius:3d}"
fahrenheit_formatted = f"{fahrenheit:5.2f}"

print(celsius_formatted), print(fahrenheit_formatted)

