import time
import math
import random
import re

player_1 = [["A", "D"], ["K", "D"]]  # ts
player_2 = [["A", "H"], ["K", "H"]]
table = [[9, "D"], ["J", "D"], ["Q", "D"], [1, "S"], [2, "S"]]  # ts
deck = []
order = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "1", "2", "3", "4"]
money_1 = 10
money_2 = 10
round_end = False
round_ = 1
pool = 0
raise_amount = 0
last_bet = 1
fold = [False, False]


def shuffle():
    card = 2
    for i in range(9):
        deck.append(str(card) + "S")
        deck.append(str(card) + "D")
        deck.append(str(card) + "H")
        deck.append(str(card) + "C")
        card += 1
    deck.append("J" + "S")
    deck.append("J" + "D")
    deck.append("J" + "H")
    deck.append("J" + "C")

    deck.append("Q" + "S")
    deck.append("Q" + "D")
    deck.append("Q" + "H")
    deck.append("Q" + "C")

    deck.append("K" + "S")
    deck.append("K" + "D")
    deck.append("K" + "H")
    deck.append("K" + "C")

    deck.append("A" + "S")
    deck.append("A" + "D")
    deck.append("A" + "H")
    deck.append("A" + "C")


def draw(person):
    if len(deck) == 0:
        x = 0
    else:
        x = random.randrange(1, len(deck))
    person.append(deck[x])

    deck.remove(deck[x])


shuffle()

# dealing-----------------------------------------------------------------------------

for i in range(2):
    # draw(player_1)ts
    # draw(player_2)
    print("ts")
print("p1 hand: " + str(player_1))
print("p2 hand: " + str(player_2))

"""
for i in range(5):
	draw(table)ts
"""
print("table: " + str(table[0]) + "," + str(table[1]) + ",X" + ",X" + ",X")
print("")

# blind-------------------------------------------------------------------------------

"""ts
#cheack, raise, fold-----------------------------------------------------------------

#player 1
while True:
        print("-------PLAYER 1-------")
        print("pool: $"+str(pool))
        print("p1 money: $"+str(money_1))
        action = input("type cheack, raise, or fold: ")

        if any(re.findall('|'.join(['fold', 'cheack', 'raise']), action)):
                if action == "cheack":
                        money_1 -= last_bet
                        pool += last_bet
                        print("p1 money: $"+str(money_1))

                if action == "raise":
                        cycle = True
                        while cycle == True:
                                try:
                                        raise_amount = int(input("how much: "))

                                        money_1 -= raise_amount + last_bet
                                        pool += raise_amount + last_bet
                                        last_bet += raise_amount


                                        cycle = False
                                except ValueError:
                                        cycle = True
                                        print("Error, can't have decimals or it is not a number")
                if action == "fold":
                        fold[0]=True
                        round_end = True
                        print("fold")
                        break
        else:
                print("")
                print("please only type fold, cheack, or raise")


#player 2
        print("-------PLAYER 2-------")
        print("pool: $"+str(pool))
        print("p2 money: $"+str(money_2))
        action = input("type cheack, raise, or fold: ")

        if any(re.findall('|'.join(['fold', 'cheack', 'raise']), action)):
                if action == "cheack":
                        money_2 -= last_bet
                        pool += last_bet
                        print("p2 money: $"+str(money_2))

                if action == "raise":
                        cycle = True
                        while cycle == True:
                                try:
                                        raise_amount = int(input("how much: "))

                                        money_2 -= raise_amount + last_bet
                                        pool += raise_amount + last_bet
                                        last_bet += raise_amount

                                        cycle = False
                                except ValueError:
                                        cycle = True
                                        print("Error, can't have decimals or it is not a number")
                if action == "fold":
                        fold[1]=True
                        round_end = True
                        print("fold")
                        break
        else:
                print("")
                print("please only type fold, cheack, or raise")

        if round_ == 1:
                print("")
                print("table: "+str(table[0])+","+str(table[1])+","+str(table[2])+",X"+",X")
        elif round_ == 2:
                print("")
                print("table: "+str(table[0])+","+str(table[1])+","+str(table[2])+","+str(table[3])+",X")
        elif round_ == 3:
                print("")
                break
        round_ += 1
"""
# showdown-------------------------------------------------------------------------------
if round_end != True:
    print("")
    print("showdown")
    print("table: " + str(table[0]) + "," + str(table[1]) + "," + str(table[2]) + "," + str(table[3]) + "," + str(
        table[4]))
    print("player: " + str(player_1))
    print("player_2: " + str(player_2))
    # ROYAL FLUSH!!!-----------------------------------------------------------------(make it better!!!)

    var = [0, 0, 0, 0, 0]
    for i in player_1 + table:
        if "S" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[0] += 1
        if "D" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[1] += 1
        if "H" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[2] += 1
        if "C" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[3] += 1
    if 5 in var:
        print("P1 ROYAL FLUSH!!! OWO")
        round_end = True
    # ------------------------------------------------------------------------------------
    var = [0, 0, 0, 0, 0]

    for i in player_2 + table:
        if "S" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[0] += 1
        if "D" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[1] += 1
        if "H" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[2] += 1
        if "C" in i:
            if any(re.findall('|'.join(["10", "J", "Q", "K", "A"]), str(i))):
                var[3] += 1
    if 5 in var:
        print("P2 ROYAL FLUSH!!! OWO")
        round_end = True

    # straght flush------------------------------------------------------------------------------------------------------------------------
    # sute sequence
    var = 0
    for i in player_1 + table:
        flush = str(order[order.index(str(i[0])):order.index(str(i[0])) + 5])
        val = 0
        x_ = 0
        for i in range(7):
            var2 = str(player_1 + table[x_][0])  # <----- cant add an int to a list
            if var2 in flush:
                val += 1
            x_ += 1

        if val == 5:
            print("straght" + flush)
            break
    # --------------------------------------------------------------------------------------------
    var = 0
    for i in player_2 + table:
        flush = str(order[order.index(str(i[0])):order.index(str(i[0])) + 5])
        val = 0
        x_ = 0
        for i in range(7):
            var2 = str(player_2 + table[x_][0])
            if var2 in flush:
                val += 1
            x_ += 1
        print(val)

        if val >= 5:
            print("straght" + flush)
            break

    # four of a kind
    # full house

    # flush
    # same sute

    # straight
    # 3 of a kind
    # 2 of a kind
    # No pair
    # same hand
elif fold[1] == True:
    print("")
    money_1 += pool
    print("p1 money: $" + str(money_1))
elif fold[0] == True:
    print("")
    money_2 += pool
    print("p2 money: $" + str(money_2))
pool = 0
