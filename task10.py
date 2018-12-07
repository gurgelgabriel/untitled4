# task 10(largest value)
print("welcome to task 10")  # print a introduction to the task
def largestvalue(inl):   # defines the function largestvalue
    a = int(input("value 1"))  # input value 1
    b = int(input("value 2"))  # input value 2
    c = int(input("value 3"))  # input value 3
    d = int(input("value 4"))  # input value 4
    listf = [a, b, c, d]  # creates a list with all the variables a,b,c,d
    if a > b and a > c and a > d:  # if a is the biggest...
        return a  # set the function value to a
    if b > a and b > c and b > d:  # if b is the biggest...
        return b  # set the function value to b
    if c > a and c > b and c > d:  # if c is the biggest...
        return c  # set the function value to c
    if d > a and d > b and d > c:  # if d is the biggest...
        return d  # set the function value to d


print(largestvalue(1))  # prints the function value on the console