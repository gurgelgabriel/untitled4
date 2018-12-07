# task 12
print("welcome to task 12")  # print a introduction to the task
import random  # ables you to use random function
list = [[], [], [], []]  # creates 4 lists inside a bigger list

rolls = int(input("how many times do you want players to roll the dice"))  # asks how many times do you want each player to roll
for x in range(0, 4):  # for x in range 0 to 4...
    for y in range(rolls):  # in range of how many times you roll
        list[x].append(random.randint(1, 6))  # put in numbers from 1 to 6 randomly in the boxes

print(list)  # prints the list that tracks the plays