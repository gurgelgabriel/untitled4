import random, linecache
a = random.randint(3, 4)
def txtreader(t):
    global a
    points = 0
    questions1 = 0
    while questions1 < 3:
        print(linecache.getline('gurgelzin.txt', a))
        ans = int(input("What's the answer?"))
        questions1 = questions1 + 1
        if ans == int(linecache.getline('baile.txt', a)):
            points = points + 1
            print("good job, you got a hard one")
            return points
        else:
            print("opps")
            return points

print(txtreader(1))




