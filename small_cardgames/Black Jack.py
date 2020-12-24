import time
import math
import random

deck = []
money = 10

def shuffle():
	card = 2
	for i in range (10):
		for i in range(4):
			deck.append(card)
		card += 1
	for i in range(3*4):
		deck.append(10)

def draw(person):
        if len(deck) == 0:
                x = 0
        else:
                x = random.randrange(1,len(deck))
        person.append(deck[x])
        
        if deck[x] == 11 and sum(person) > 21:
                person[-1] = 1
        elif 11 in person and sum(person)>21:
                person[person.index(11)] = 1

        deck.remove(deck[x])
        time.sleep(0.2)

print("Black Jack")

round_ = 0
for i in range(10):

	if len(deck) <= 16:
		shuffle()
		print("shuffled")
		
	player = []
	dealer = []
	end_game = False

	print("")
	round_ += 1
	print("round: "+str(round_))
	print("-------------------")
	print("money: $"+str(money))
	#round start------------------------------------------------------------------------------------------------------------------------------------
	for i in range(2):
		draw(player)
		draw(dealer)
	print("player: "+str(player)+" "+str(sum(player)))
	print("dealer: "+str(dealer))


	#hit or stay-------------------------------------------------------------------------------------------------------------------------------------

	while sum(player) < 21:#sum of hand is < 21
		action = input("type hit or stay: ")
		if action == "hit":
			draw(player)
			print("player: "+str(player)+" "+str(sum(player)))
		if action == "stay":
			break

	if sum(player) > 21: #sum of hand is > 21
		print("bust")
		print("you lose")
		money -= 1
		end_game = True
	else:#dealer------------------------------------------------------------------------------------------------------------------------------------
		while sum(dealer) <= 16: #dealer <= 16
			if sum(dealer) <= 16: #sum of dealer <= 16
				draw(dealer)
				print("dealer: "+str(dealer))
			elif sum(dealer) > 16: #sum of dealer >16
				print("dealer: "+str(dealer))
				break
		if sum(dealer) > 21: #sum of dealer > 21
			print("bust")
			print("you win")
			money += 1
			end_game = True
	#show down---------------------------------------------------------------------------------------------------------------------------------------
	if end_game == False:
		print(" ")
		print("player: "+str(player))
		print("dealer: "+str(dealer))
		if sum(player) > sum(dealer):#sum of player > dealer
			if len(player) == 2 and sum(player) == 21:
				print("BLACK JACK!!!")
				time.sleep(0.5)
			print("you win")
			money += 1
		elif sum(player) < sum(dealer): #sum of player < dealer
			print("you lose")
			money -= 1
		elif sum(player) == sum(dealer): #sum of player == dealer
			print("draw")
			
	time.sleep(0.5)

print("your money: $"+str(money))
