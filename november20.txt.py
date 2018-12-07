q1m = "23+11 is equal to... 1)35, 2)33, 3)34"
q2m = "11-2 is equal to... 1)9, 2)-9, 3) 5"
q3m = "square of 2 is equal to... 1) 10, 2) -4, 3) 4"
q21m = "3/0 is equal to... 1) math error, 2) infinite, 3) 0"
q22m = "100*0 is equal to... 1) math error, 2)100, 3)0"
q23m = "square root of 2 is... 1)2, 2)irracional, 3)4"
a21 = 3
a22 = 1
a23 = 3
a71 = 1
a72 = 3
a73 = 2
level12 = [q1m, q2m, q3m]
level22 = [q21m, q22m, q23m]
math1 = [level12, level22]
answer12 = [a21, a22, a23]
answer22 = [a71, a72, a73]
matha = [answer12, answer22]
import random
def math(r):
    global matha, math1
    questions = 0
    points = 0
    while questions < 6:
        a = random.randint(0, 1)
        b = random.randint(0, 2)
        print(math1[a][b])
        pergunta = int(input("answer"))
        if pergunta == matha[a][b]:
            points = points + 1
            print("wright answer")
            questions = questions + 1
        else:
            print("wrong answer")
            questions = questions + 1
    return points

print(math(1))


