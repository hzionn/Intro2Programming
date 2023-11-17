"""
英文單字字典

讓使用者能夠以輸入編號來查看單字翻譯。
當使用者輸入錯誤時，給予提示。
"""

print("1. 蘋果")
print("2. 香蕉")
print("3. 橘子")
print("4. 葡萄")

number = int(input("請輸入想查詢的單字號碼:"))

if 1 <= number <= 4:
    if number == 1:
        print("Apple")
    if number == 2:
        print("Banana")
    if number == 3:
        print("Orange")
    if number == 4:
        print("Grape")
else:
    print("請輸入介於 1~4 的數字")

