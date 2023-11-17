"""
Write a function that takes string content as input, and print the string content in message block.
- return nothing if the content is empty
- print content in block if content is not empty
"""


def string_block(message: str):
    length = len(message)
    if length > 0:
        print("#" * (length + 4))
        print("!", message, "!")
        print("#" * (length + 4))
    else:
        return


message = input("Enter your message: ")
string_block(message)
