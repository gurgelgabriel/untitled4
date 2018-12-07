# task 6(shopping list)
print("welcome to task 6")  # print a introduction to the task
list_2 = []  # creates a list
print("you need to buy: potatos, apples, bananas, ice cream ")  # print what you need to buy
list_1 = ["potatos", "apples", "bananas", "ice cream"]  # creates a second list
while list_1[0] not in list_2 or list_1[1] not in list_2 or list_1[2] not in list_2 or list_1[3] not in list_2:  # creates a while loop until "list" have all those thinks
    inpu_1 = int(input("press 0 to 3 on the order we post the list for the item you got"))  # ask the user what he got
    if inpu_1 == 0:  # if the user anserw 0
        list_2.insert(0, "potatos")  # you add potatos as the first item of the list
    if inpu_1 == 1:  # if the user anserw 1
        list_2.insert(1, "apples")  # you add apples as the second item of the list
    if inpu_1 == 2:  # if the user anserw 2
        list_2.insert(2, "bananas")   # you add bananas as the third item of the list
    if inpu_1 == 3:  # if the user anserw 3
        list_2.insert(3, "ice cream")  # you add ice cream as the fourth item of the list
    print("you have", list_2)  # print what you have inside the while loop so every time you get somethink you will know what you still need













