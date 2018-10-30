print("welcome to py poker if you get to 0 you lose; if you want to leave press 1 in the end of a round")  # instructions about how to run the program + introduction
initial_cash = 100  # the amount of money you start
print("you have 100 bucks")  # tells the player how much it have
import itertools, random  # permit us to use a intertool and a random fuction
rerun = 0  # set a value to the variable rerun
cards_table = []  # to make that a list
player_2 = []  # to make that a list
while rerun == 0:  # allow us to loop the program until rerun = 0


    if initial_cash <= 0:  # if you run out of money you lose
       print("you lose")  # print the message you lose
       rerun = int(input("press 1 to restart"))  # if you press 1 you restart the game
    else:  # if you don t run out of money then...
        deck_cards = list(itertools.product(range(1, 13), ['Spade', 'Heart', 'Diamond', 'Club']))  # makes a list with the relation between number of cards and it s suits
    import random  #import a random function
    random.shuffle(deck_cards)  # makes you deck random, basicly shufles it
    for x in range(2):  # makes the the variable below act 2 times
        your_cards = deck_cards[x][0], "of", deck_cards[x][1]  # stick a value to the variable your_cards, those are the cards of your hand
        deck_cards.remove(deck_cards[x])  # make this variable value not repeat
        print(print("your hand is"), your_cards)  # print what cards you have in hand
    print("splash = 2 bucks")  # tell you the minimum you need to pay to enter the game
    cash_0 = int(input("how much will you pay?"))  # ask how much money will you pay
    if cash_0 < 2:  # in case you pay less then 2 then...
        print("you won't play this round")  # a message you saying that you play this round apear
        cash_1 = initial_cash - cash_0  # in case you don t pay enough how much money will you still have
        initial_cash = cash_1  # initial value is the value you start each round, so if you lose the next round you will have initial cash that equal the previus varieble, cash 1
        print("you have", initial_cash)  # tells you how much money you still have
        rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # if you don't want to pay on a round you can both play next round or get out of the game
    if cash_0 >= 2:  # if you pay more more = then 2...
        cash_3 = initial_cash - cash_0  # formula of how much you still have
        print("your cash is", cash_3)  # print how much you still have
        for x in range(3):  # to repeat it three times
            cards_table.append([deck_cards[x][0], "of", deck_cards[x][1]])  # the variable cards_table represent that list
            deck_cards.remove(deck_cards[x])  # don't allow cards that have already been used repeat again
        print("cards in the table are", cards_table)  # print what are the cards in the table
        first_player = random.randint(0, 10)  # creates a varieble for the other players random bets from 0 to 10
        print("someone payed", first_player)   # print the table bet
        cash_2 = int(input("how much will you pay?"))  # asks how much will you pay for that round
        if cash_2 < first_player:  # if you pay less then the other players...
            print("next round")  # a message saying next round will be printed
            cash_1 = initial_cash - cash_0 - cash_2  # a formula for how much money you still have
            initial_cash = cash_1  # set the cash for next round the value you still have
            print("you have", initial_cash)  # print how much you have
            rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # asks you if you want to play next round or abandon the game
        if cash_2 >= first_player:  # if you pay the same or more than other players on table...
            second_player = random.randint(0, 2)  # randomly set a value for a variable showing how many players didn't bet
            number_players = 5 - second_player  # formula for number of players remaining
            cards_table1 = deck_cards[x][0], "of", deck_cards[x][1]  # set a next card to go on table
            deck_cards.remove(deck_cards[x])  # take this card of the list, don't allow it to repeat itself
            print("you covered it. Next card is", cards_table1)  # tell you what the next card is
            print("number of players remaining", number_players)  # tell you how many players remain
            cash = cash_3 - cash_2  # formula for how many money you have
            print("you have", cash)  # print the amount of money you have
            first_player2 = random.randint(0, 10)  # set a random value from 0 to 10 to a variable that represent other players bets
            print("someone payed", first_player2)  # prints the value of the other people on table bets
            cash_4 = int(input("how much will you pay?"))  # ask you how much money you will pay
            second_player2 = random.randint(0, 2)  # set a random number for the variable the represent how many players didn't bet
            number_players2 = number_players - second_player2  # formula for number of players remaining
            print("number of players remaining", number_players2)  # print the number of players remaining
            if number_players2 <= 1:  # in case there are equal or less number of players than 1....
                print("next round")  # send a message telling next round
                cash_1 = cash + cash_2*number_players + cash_0*5 + cash_4*number_players2  # formula for how much you still have
                initial_cash = cash_1  # set the amount of money you will start next round
                print("you have", initial_cash)  # print the amount of money you still have
                rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # asks if you want to play next round or stop playing
            if cash_4 < first_player2:  # in case you pay less then the rest of the table...
                print("next round")  # send a message telling next round
                cash_1 = cash - cash_4  # formula for how much money you still have
                initial_cash = cash_1  # set the amount of money you will start next round
                print("you have", initial_cash)  # print how much will you start next round
                rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # asks if you want to play next round or stop playing
            if cash_4 >= first_player2:  # if you pay equal or more then the other players
                cards_table2 = deck_cards[x][0], "of", deck_cards[x][1]  # creates another card for the table
                deck_cards.remove(deck_cards[x])  # remove this card from the deck so it doesnt repeat
                print("you covered it, final round! next card is", cards_table2)  # print what the next card is
                cash_5 = cash - cash_4  # formula for how much money you have
                print("you have", cash_5)  # print the amount of money you have
                second_player3 = random.randint(0, 1)  # set a random number for the variable the represent how many players didn't bet
                number_players3 = number_players2 - second_player3  # formula for how many players remain
                print("number of players remaining", number_players2)  # print the number of players remaining
                if number_players3 <= 1:  # in case you have insufficient number of players...
                        cash_1 = cash_5 + cash_4*number_players2 + cash_0*5 + cash_2*number_players  # formula for how much money you have
                        initial_cash = cash_1  # set how much you have for next round
                        print("you have", initial_cash)  # print how much you still have
                if number_players3 > 1:  # if you a sufficient number of players...
                    first_player3 = random.randint(0, 30)  # set a random value for other players bet from 1 to 30
                    print("someone payed", first_player3)  # print how much other players bet
                    cash_6 = int(input("how much will you pay?"))  # ask how much will you bet
                    if cash_6 < first_player3:  # if you bet is less then the table value
                        print("next round, you have", cash_5)  # print how much you have and warns you for next round
                        initial_cash = cash_5  # set how much will you have for next round
                        rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # asks if you want to play next round or stop playing
                    if cash_6 >= first_player3:  # if you bet the same or more than the table value
                        print("showdown")  # send a message showdown
                        print("the cards in the table are", cards_table, cards_table1, cards_table2)  # shows all the cards in the table again
                        for i in range(number_players3*2):  # repeat the action for the number of players times 2
                            player_2.append([deck_cards[x][0], "of", deck_cards[x][1]])  # the varieble is represented as a list, so it has to be repeat as a list
                            deck_cards.remove(deck_cards[x])  # don't allow does cards to repeat
                        print("other player cards", player_2)  # print the cards the other players have
                        victorie = int(input(" if you won press 0, if not press 1"))  # by your knowlege you tell the game if you won or not
                        if victorie == 0:  # if  you press 0, you won...
                            cash_1 = cash_5 + cash_6 * number_players3 + cash_4 * number_players2 + cash_0 * 5 + cash_2 * number_players2  # formula for how much money you still have
                            initial_cash = cash_1  # set how much money will you start next round
                            print("you have", initial_cash)  # tell you how much money you have
                            rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # asks you if you want to play next round or abandon the game
                        else:  # in case you lost...
                            cash_1 = cash_5 - cash_6  # how much you have
                            initial_cash = cash_1  # set the money you have for nex round
                            print("you have", initial_cash)  # print how much money you have
                            rerun = int(input("do you want to keep playing? if yes press 0, if not press 1"))  # asks you if you want to play next round or abandon the game




























    # deck_cards.index(random_card) tell you the index of the random card

