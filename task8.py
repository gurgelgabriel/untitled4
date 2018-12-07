# task 8(dice)
print("welcome to task 8")  # print a introduction to the task
list = []  # creates a empty list
import random  # able you to use random function
dice_rolls = int(input("how many times will you roll"))  # asks you how many times you rolled
for x in range(dice_rolls):  # for loop in the range of variable "rolls"
    l = random.randint(1, 6)  # set a random value to variable l
    if l == 1:  # in case l is equal to 1....
        list.insert(0, "1")  # insert "1" at index 0
    if l == 2:  # in case l is equal to 2....
        list.insert(0, "2")  # insert "2" at index 0
    if l == 3:  # in case l is equal to 3....
        list.insert(0, "3")  # insert "3" at index 0
    if l == 4:  # in case l is equal to 4....
        list.insert(0, "4")  # insert "4" at index 0
    if l == 5:  # in case l is equal to 5....
        list.insert(0, "5")  # insert "5" at index 0
    if l == 6:  # in case l is equal to 6....
        list.insert(0, "6")  # insert "6" at index 0
print(list)  # prints list at the console