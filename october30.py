# task 9(the pivot list)
print("welcome to task 9")  # print a introduction to the task
def pivotlist(inlist, number):  # define a function and it parameters
    list = []  # creates a list
    for x in inlist:  # for the values in "inlist"
        if x < number:  # if x is smaler then parameter number..
            list.append(x)  # you put the x inside your list
    return list  # set the value of list and finish the function


inlist = [1, 2, 3, 4, 5, 6 ,7 ,8 ,18, 81, 100]  # creates a list inside the parameter "inlist"
number = int(input("chose a number"))  # input a value to the parameter "number"
print(pivotlist(inlist, number))  # calls the function and prints it on the console