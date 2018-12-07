h1 = "Which of those weren't ever elected as president? 1)Dilma 2)Temer 3)Bolsonaro"      # questions stored in variables
h2 = "What was the year of signing of the aurea law? 1)1900 2)1888 3)1781"  # questions stored in variables
h3 = "Which of those weren't a Santos Dummont Invention? 1)Airplane 2)Wristwatch 3)ethanol fuel 4)bottle"  # questions stored in variables
h21 = "Which of those didnt suffer from impeachment?1 )lula 2) Dilma 3) Color"  # questions stored in variables
h22 = "Who is the richest brazilian ever? 1)Jorge Paulo Leiman 2) Safra 3) Santos Dummont"  # questions stored in variables
h23 = "What was the name of brazilian currency before 'reais'? 1)Cruzeiro 2)Dollars 3)Euros"  # questions stored in variables
listq1 = [h1, h2, h3]  # list with level one questions
listq2 = [h21, h22, h23]  # list with level 2 questions
hist1 = [listq1, listq2]  # 2d list with level one and 2 questions
a111 = 2  # answer stored in a varieble
a112 = 4  # answer stored in a varieble
a113 = 1  # answer stored in a varieble
a121 = 1  # answer stored in a varieble
a122 = 1  # answer stored in a varieble
a123 = 1  # answer stored in a varieble
list11 = [a111, a112, a113]  # list with level 1 answers
list12 = [a121, a122, a123]  # list with level 2 answers
hista = [list11, list12]  # 2d list with level 1 and 2 answers

q1m = "23+11 is equal to... 1)35, 2)33, 3)34"  # questions stored in variables
q2m = "11-2 is equal to... 1)9, 2)-9, 3) 5"  # questions stored in variables
q3m = "square of 2 is equal to... 1) 10, 2) -4, 3) 4"  # questions stored in variables
q21m = "3/0 is equal to... 1) math error, 2) infinite, 3) 0"  # questions stored in variables
q22m = "100*0 is equal to... 1) math error, 2)100, 3)0"  # questions stored in variables
q23m = "square root of 2 is... 1)2, 2)irracional, 3)4"  # questions stored in variables
a21 = 3  # answer stored in a varieble
a22 = 1  # answer stored in a varieble
a23 = 3  # answer stored in a varieble
a71 = 1  # answer stored in a varieble
a72 = 3  # answer stored in a varieble
a73 = 2  # answer stored in a varieble
level12 = [q1m, q2m, q3m]  # list with level one questions
level22 = [q21m, q22m, q23m]  # list with level 2 questions
math1 = [level12, level22]  # 2d list with level one and 2 questions
answer12 = [a21, a22, a23]  # list with level 1 answers
answer22 = [a71, a72, a73]  # list with level 2 answers
matha = [answer12, answer22]  # 2d list with level 1 and 2 answers
h31 = "What is the name of scooby doo owner in portuguese? 1) Ben 2) Salsicha 3) Bro"  # questions stored in variables
h32 = "What is the current France president? 1) Macron 2) Trump 3) Bolsonaro"  # questions stored in variables
h33 = "What canada current prime minister? 1) Justin Troudle 2) Macron 3) Bolsonaro "  # questions stored in variables
h321 = "What is the largest city in Brazil? 1) Rio de janeiro 2) Sao paulo 3) Salvador"  # questions stored in variables
h322 = "Which of those is not part of Amazon? 1) Brazil 2) bolivia 3) El Salvador"  # questions stored in variables
h323 = "Who is the richest man in the world? 1) Jeff Bezos(Amazon owner) 2) Bill Gates 3) Mark Zuckemberg "  # questions stored in variables
listq31 = [h31, h32, h33]  # list with level one questions
listq32 = [h321, h322, h323]  # list with level 2 questions
genknow1 = [listq31, listq32]  # 2d list with level one and 2 questions
a311 = 2  # answer stored in a varieble
a312 = 1  # answer stored in a varieble
a313 = 1  # answer stored in a varieble
a321 = 2  # answer stored in a varieble
a322 = 3  # answer stored in a varieble
a323 = 1  # answer stored in a varieble
list31 = [a311, a312, a313]  # list with level 1 answers
list32 = [a321, a322, a323]  # list with level 2 answers
genknowa = [list31, list32]  # 2d list with level 1 and 2 answers
h41 = "Who is the most victorious swimmer of all time? 1) Micheal Phealps 2) Cesar Cielo 3) Micheal jordan"  # questions stored in variables
h42 = "Who won 2002 soccer world cup? 1) France 2) Germany 3) Brazil"  # questions stored in variables
h43 = "Which of those Brazilians play on NBA? 1) Lucas Zibecchi 2) Nene 3) Joao Bobao"  # questions stored in variables
h421 = "What is the Usain Bolt currently competing on? 1) Soccer 2) Basketball 3) Running"  # questions stored in variables
h422 = "Who won the 2014 world surf league1) Kelly slater 2) Gabriel Medina 3) Jonh Jonh Florence"  # questions stored in variables
h423 = "Who is the biggest flamengo idol 1) Zico 2) Ronaldinho 3) Imperador"  # questions stored in variables
listq41 = [h41, h42, h43]  # list with level one questions
listq42 = [h421, h422, h423]   # list with level 2 questions
sports1 = [listq41, listq42]  # 2d list with level one and 2 questions
a411 = 1  # answer stored in a varieble
a412 = 3  # answer stored in a varieble
a413 = 2  # answer stored in a varieble
a431 = 1  # answer stored in a varieble
a432 = 2  # answer stored in a varieble
a433 = 1  # answer stored in a varieble
list41 = [a411, a412, a413]  # list with level 1 answers
list42 = [a431, a432, a433]  # list with level 2 answers
spoertsa = [list41, list42]  # 2d list with level 1 and 2 answers


questionsasked = []  # a list that is used later
randomchosen = []  # a list used later

import random, linecache  # allows us to use functions such as random and linecache
questions = 0  # creates set the variable questions to 0
points = 0  # creates and set the variable points to 0
print("Welcome to Quizmaster.py")  # prints introduction
print("our game consist of 4 categories, each categorie have 8 questions, if you get it right a point, if not 0")  # prints introduction
categorie = int(input("press 1 for history, 2 for math, 3 for general knowlage and 4 for sport"))  # ask the user which categorie they want, with the variable categorie
if categorie == 1:  # in case categorie is equal to 1...
    print("you choose history")  # prints the category you choose

    # Take note that this function is repeated multiple times, only changing the function name, variables names and questions

    def hist(r):  # creates a function
        global hista, hist1, questionsasked, questions, points  # allow us to use those variables
        while questions < 6:  # if the variable questions is less than 6 keep running
            a = random.randint(0, 1)  # random value, or 0 or 1 to variable "a"
            b = random.randint(0, 2)  # random value, 0, 1 or 2 to variable "b"
            while hist1[a][b] in questionsasked:  # if the question in the variable hist1 is inside list questionsasked, keep running
                a = random.randint(0, 1)  # set a random value, 0 or 1 to variable "a"
                b = random.randint(0, 2)  # random value 0, 1 or 2 to variable "b"
            questionsasked.append(hist1[a][b])  # you put the question you asked inside the list questionsasked
            print(hist1[a][b])  # prints your question
            pergunta = int(input("answer"))  # asks you what is the answer
            if pergunta == hista[a][b]:  # if your answer is wright
                points = points + 1  # increase points by one
                print("wright answer")  # prints "wright aswer"
                questions = questions + 1  # increase question by one
            else:  # in case you got it wrong...
                print("wrong answer")  # prints "wrong answer"
                questions = questions + 1  # increases questions by one
        return points  # return how many points you have

    print(hist(1))  # calls your function

    # Take note that this function is repeated multiple times, only changing the function name, files names and questions

    def txtreader(t):  # defines the function
        global a, points, questions, randomchosen  # allows you to use these variables
        while questions < 8:  # if questions are less then 8 keep running
            a = random.randint(3, 4)  # a random value, 3 or 4 to variable "a"
            while a in randomchosen:  # if "a" is inside the list randomchoosen, keep running
                a = random.randint(3, 4)  # a random value, 3 or 4 to variable "a"
            randomchosen.append(a)  # insert a in the list randomchoosen
            print(linecache.getline('gurgelzin.txt', a))  # prints a question from the textfile gurgelzin.txt
            ans = int(input("What's the answer?"))  # asks you what is the wright answer
            questions = questions + 1  # increase questions by one
            if ans == int(linecache.getline('baile.txt', a)):  # if your answer is correct then...
                points = points + 1  # increase points by one
                print("good job, you got a hard one")  # prints that you've got it right
            else:  # in case you got it wrong...
                print("opps")  # prints opps
        return print("points =", points)  # returns your points


    (txtreader(1))  # calls your function

elif categorie == 2:
    print("you choose math")
    def math(r):
        global matha, math1, questionsasked, questions, points
        while questions < 6:
            a = random.randint(0, 1)
            b = random.randint(0, 2)
            while math1[a][b] in questionsasked:
                a = random.randint(0, 1)
                b = random.randint(0, 2)
            questionsasked.append(math1[a][b])
            print(math1[a][b])
            pergunta = int(input("answer"))
            if pergunta == matha[a][b]:
                points = points + 1
                print("wright answer")
                questions = questions + 1
            else:
                print("wrong answer")
                questions = questions + 1
        return print("points =", points)

    (math(1))


    def txtreader2(t):
        global a, points, questions, randomchosen
        while questions < 8:
            a = random.randint(7, 8)
            while a in randomchosen:
                a = random.randint(7, 8)
            randomchosen.append(a)
            print(linecache.getline('gurgelzin.txt', a))
            ans = int(input("What's the answer?"))
            questions = questions + 1
            if ans == int(linecache.getline('baile.txt', a)):
                points = points + 1
                print("good job, you got a hard one")
            else:
                print("opps")
        return print("points =", points)


    (txtreader2(1))
elif categorie == 3:
    print("you choose general knowlage")
    def genknow(r):
        global genknowa, genknow1, questionsasked, points, questions
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
        return print("points =", points)


    (genknow(1))

    def txtreader3(t):
        global a, points, questions, questionsasked
        while questions < 8:
            a = random.randint(11, 12)
            while a in randomchosen:
                a = random.randint(11, 12)
            randomchosen.append(a)
            print(linecache.getline('gurgelzin.txt', a))
            ans = int(input("What's the answer?"))
            questions = questions + 1
            if ans == int(linecache.getline('baile.txt', a)):
                points = points + 1
                print("good job, you got a hard one")
            else:
                print("opps")
        return print("points =", points)

    txtreader3(1)
elif categorie == 4:
    print("you choose sport")
    def sport(r):
        global spoertsa, sports1, questionsasked, questions, points
        questions = 0
        points = 0
        while questions < 6:
            a = random.randint(0, 1)
            b = random.randint(0, 2)
            while sports1[a][b] in questionsasked:
                a = random.randint(0, 1)
                b = random.randint(0, 2)
            questionsasked.append(sports1[a][b])
            print(sports1[a][b])
            pergunta = int(input("answer"))
            if pergunta == spoertsa[a][b]:
                points = points + 1
                print("wright answer")
                questions = questions + 1
            else:
                print("wrong answer")
                questions = questions + 1
        return print("points =", points)


    (sport(1))

    def txtreader4(t):
        global a, points, questions
        while questions < 8:
            a = random.randint(15, 16)
            while a in randomchosen:
                a = random.randint(15, 16)
            randomchosen.append(a)
            print(linecache.getline('gurgelzin.txt', a))
            ans = int(input("What's the answer?"))
            questions = questions + 1
            if ans == int(linecache.getline('baile.txt', a)):
                points = points + 1
                print("good job, you got a hard one")
            else:
                print("opps")
        return print("points =", points)

    txtreader4(2)

# THE 2 FUNCTIONS KEEP REPEATING UNTIL HERE!!!

print("Now for 2 extra points you will have to answer a question that is not nescessaryly from your categorie")  # prints you have one extra question
print("if you are lucky you might get a question you were already asked")  # say that you've might have seen this question
def extrapoints(n):  # defines a function
    global points  # allows you to use points
    a = random.randint(1, 8)  # set a to a random value between 1 and 8
    print(linecache.getline('newquestions.txt', a))  # prints your question
    ans = int(input("what is the answer?"))  # asks you for an answer
    if ans == int(linecache.getline('aswers.txt', a)):  # in case you get the right answer...
        points = points + 2  # increase points by two
        print("oh yeah!")  # prints oh yeah
    else:  # in case you get it wrongly...
        print("oh no!")  # prints "oh no"
    return print("points =", points)  # returns points

extrapoints(2)  # calls your function

print("unfortunaly you've fineshed your game, but good job")  # prints a message telling your game finished




