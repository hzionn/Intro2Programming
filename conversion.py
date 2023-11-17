"""
單位轉換
"""


def convert_units(value, from_unit, to_unit):
    # 單位轉換邏輯，可以根據需要添加更多單位
    if from_unit == "cm" and to_unit == "inch":
        return value * 0.393701
    elif from_unit == "inch" and to_unit == "cm":
        return value / 0.393701
    else:
        return None


while True:
    # 接收用戶輸入
    user_input = input("輸入轉換指令（例如 '15 cm inch'）或輸入 'exit' 以結束：")

    # 檢查是否為結束指令
    if user_input.lower() == 'exit':
        print("程式結束")
        break

    # 分解用戶輸入
    parts = user_input.split()

    # 檢查輸入格式
    if len(parts) != 3:
        print("輸入格式錯誤，請重新輸入")
        continue

    # 提取數值和單位
    try:
        value = float(parts[0])
        from_unit = parts[1]
        to_unit = parts[2]

        # 進行單位轉換
        converted_value = convert_units(value, from_unit, to_unit)
        if converted_value is not None:
            print(f"{value} {from_unit} 等於 {converted_value} {to_unit}")
        else:
            print("不支援的單位轉換")

    except ValueError:
        print("無效的數值，請重新輸入")

