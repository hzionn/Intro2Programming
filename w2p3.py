"""
《像極了愛情》
"""

# DRY: Dont Repeat Yourself
message = "請你給我一句優美的句子："
user_input_1 = input(message)
user_input_2 = input(message)
user_input_3 = input(message)
user_input_4 = input(message)
user_input_5 = input(message)

print("=" * 50)  # divider
print(user_input_1)
print(user_input_2)
print(user_input_3)
print(user_input_4)
print(user_input_5)

print("像極了愛情")
print("=" * 50)


# another way to do it
# store user's inputs into a list with loop and list comprehension
user_input = [input("請你給我一句優美的句子：") for _ in range(5)]

print("=" * 50)
# print input by loop through the list
for sentence in user_input:
    print(sentence)
print("像極了愛情")

