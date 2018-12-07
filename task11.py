# task 11(merge list)
print("welcome to task 11")  # print a introduction to the task
def merge(list1, list2):  # define a function with 2 parameters
    list3 = []  # creates a list
    list = list1 + list2  # creates a list that have two lists, "list1", and "list2"
    for x in range(len(list)):  # for loop in range of how many elements you have
        list3.insert(0, max(list))  # puts the max value of list at index 0 in "list3"h
        list.remove(max(list))  # remove the max values from "list"
    return list3  # ends the function setting the value as list3




list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]  # the "list1"
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]  # the "list2"
print(merge(list1, list2))  # prints the function
