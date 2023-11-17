"""
帳號密碼驗證流程：

當使用者輸入帳號、密碼，且驗證正確時，
就顯示 “帳密正確，歡迎加入系統”
否則顯示 “帳密錯誤，無法使用系統” 的訊息。
"""

# the account and password that saved in your database
# there is no need to save the password in integer
# we are not gonna use it for calculation
# therefore we dont need to convert input() into integer
database = {
    "zionn": "1234",
    "jone": "4453",
    "watson": "1111",
}

input_name = input("please enter your username: ")
input_pwd = input("now enter your password: ")

if (input_name in database) and (input_pwd == database[input_name]):
    print("welcome back to our system")
else:
    print("wrong password or username")
