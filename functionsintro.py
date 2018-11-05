def large_num(a, b, c):  # define the value of the function large num
    if a > b and a > c:  # in case parameter a is the biggest
        return a  # The function will assume a value equal to a
    elif b > a and b > c:  # in case parameter b is the biggest
        return b  # The function will assume a value equal to a
    else:  # in case parameter a is the biggest
        return c  # The function will assume a value equal to a

print(large_num(int(input("num1")), int(input("num2")), int(input("num3"))))  # asks you the values you want to give for each parameter and finish your function


import random  # enables you to use random
def sumdice(dice, rolls):  # define a function called sumduce with the parameters dice and rolls
    sum = 0  # set variable sum to 0
    for x in range(1, rolls):  # the number of times you will roll
        sum = sum + random.randint(1, dice)  # uses the random function to set a new value to sum
    return sum  # the function will assume a value equal to sum

print(sumdice(int(input("how many times you rolled?")), int(input("how many sides you have?"))))  # ends the function and asks how many sides you have and how many times you rolled