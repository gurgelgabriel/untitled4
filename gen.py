                h31 = "What is the name of scooby doo owner in portuguese 1) Ben 2) Salsicha 3) Bro"                h31 = "What is the name of scooby doo owner in portuguese 1) Ben 2) Salsicha 3) Bro"
h32 = "What is the current France president 1) Macron 2) Trump 3) Bolsonaro"
h33 = "What canada current prime minister 1) Justin Troudle 2) Macron 3) Bolsonaro "
h321 = "What is the largest city in Brazil 1) Rio de janeiro 2) Sao paulo 3) Salvador"
h322 = "Which of those is not part of Amazon 1) Brazil 2) bolivia 3) El Salvador"
h323 = "Who is the richest man in the world 1) Jeff Bezos(Amazon owner) 2) Bill Gates 3) Mark Zuckemberg "
listq31 = [h31, h32, h33]
listq32 = [h321, h322, h323]
genknow1 = [listq31, listq32]
a311 = 2
a312 = 1
a313 = 1
a321 = 2
a322 = 3
a323 = 1
list31 = [a311, a312, a313]
list32 = [a321, a322, a323]
genknowa = [list31, list32]
questionsasked = []
import random
def genknow(r):
    global genknowa, genknow1
    questions = 0
    points = 0
    while questions < 6:
        a = random.randint(0, 1)
        b = random.randint(0, 2)
        while genknow1[a][b] in questionsasked:
             a = random.randint(0, 1)
             b = random.randint(0, 2)
        questionsasked.append(genknow1[a][b])
        print(genknow1[a][b])
        pergunta = int(input("answer"))
        if pergunta == genknowa[a][b]:
            points = points + 1
            print("wright answer")
            questions = questions + 1
        else:
            print("wrong answer")
            questions = questions + 1
    return points

print(genknow(1))
h32 = "What is the current France president 1) Macron 2) Trump 3) Bolsonaro"
h33 = "What canada current prime minister 1) Justin Troudle 2) Macron 3) Bolsonaro "
h321 = "What is the largest city in Brazil 1) Rio de janeiro 2) Sao paulo 3) Salvador"
h322 = "Which of those is not part of Amazon 1) Brazil 2) bolivia 3) El Salvador"
h323 = "Who is the richest man in the world 1) Jeff Bezos(Amazon owner) 2) Bill Gates 3) Mark Zuckemberg "
listq31 = [h31, h32, h33]
listq32 = [h321, h322, h323]
genknow1 = [listq31, listq32]
a311 = 2
a312 = 1
a313 = 1
a321 = 2
a322 = 3
a323 = 1
list31 = [a311, a312, a313]
list32 = [a321, a322, a323]
genknowa = [list31, list32]
questionsasked = []
import random
def genknow(r):
    global genknowa, genknow1
    questions = 0
    points = 0
    while questions < 6:
        a = random.randint(0, 1)
        b = random.randint(0, 2)
        while genknow1[a][b] in questionsasked:
             a = random.randint(0, 1)
             b = random.randint(0, 2)
        questionsasked.append(genknow1[a][b])
        print(genknow1[a][b])
        pergunta = int(input("answer"))
        if pergunta == genknowa[a][b]:
            points = points + 1
            print("wright answer")
            questions = questions + 1
        else:
            print("wrong answer")
            questions = questions + 1
    return points

print(genknow(1))