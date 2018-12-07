h41 = "Who is the most victorious swimmer of all time? 1) Micheal Phealps 2) Cesar Cielo 3) Micheal jordan"
h42 = "Who won 2002 soccer world cup? 1) France 2) Germany 3) Brazil"
h43 = "Which of those Brazilians play on NBA? 1) Lucas Zibecchi 2) Nene 3) Joao Bobao"
h421 = "What is the Usain Bolt currently competing on? 1) Soccer 2) Basketball 3) Running  "
h422 = "Who won the 2014 world surf league? 1) Kelly slater 2) Gabriel Medina 3) Jonh Jonh Florence"
h423 = "Who is the biggest flamengo idol? 1) Zico 2) Ronaldinho 3) Imperador"
listq41 = [h41, h42, h43]
listq42 = [h421, h422, h423]
sports1 = [listq41, listq42]
a411 = 1
a412 = 3
a413 = 2
a431 = 1
a432 = 2
a433 = 1
list41 = [a411, a412, a413]
list42 = [a431, a432, a433]
spoertsa = [list41, list42]
questionsasked = []
import random
def sport(r):
    global spoertsa, sports1, questionsasked
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
    return points

print(sport(1))
