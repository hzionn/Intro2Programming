def intName(number):
    """"""

    part = number  # the part that still needs to be converted
    name = ""  # the name of the number

    if part >= 100:
        name = digitName(part // 100) + " hundred"
        part = part % 100

    if part >= 20:
        name = name + " " + tensName(part // 10)
        part = part % 10
    elif part >= 10:
        name = name + " " + teenName(part)
        part = 0

    if part > 0:
        name = name + " " + digitName(part)

    return name


def digitName(n) -> str:
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    else:
        return ""


def tensName(n) -> str:
    if n == 2:
        return "twenty"
    elif n == 3:
        return "thirty"
    else:
        return ""


def teenName(n) -> str:
    if n == 3:
        return "three"
    elif n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    else:
        return ""


print(intName(123))
