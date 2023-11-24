# here we define a function
def hello():
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")

    if gender == "male":
        print(f"Hello {name} 先生")
    elif gender == "female":
        print(f"Hello {name} 小姐")
    else:
        print("can only enter male or female")


# and here we call the function
hello()
