def large_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(large_num(int(input("num1")), int(input("num2")), int(input("num3"))))


import random
dice = int(input("how many sids you have"))
rolls = int(input("how many times will you roll"))
def sumdice(dice, rolls):
    sum = 0
    for x in range(1, rolls):
        sum = sum + random.randint(1, dice)
    return sum

print(sumdice(1, 5))