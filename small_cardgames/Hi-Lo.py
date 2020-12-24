print("Card Counting")
print("NOTE: put spaces inbetween numbers")
Running_Count = 0
while True:
	dealer = []
	player = []

	player = list(map(int, input("player cards: ").split()))

	dealer = list(map(int, input("dealer cards: ").split())) 

	total = dealer + player

	for x in total:
		if x < 7:
			Running_Count += 1
		if x > 9:
			Running_Count -= 1

	print("Running Count: "+str(Running_Count))
