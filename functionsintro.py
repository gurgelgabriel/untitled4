def large_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(large_num(int(input("num1")), int(input("num2")), int(input("num3"))))


def sumdice(dice, numbrolls):
    value = dice*numbrolls