both = input("Enter the plays: ").split("@")

player_a = both[0].split(" ")

player_b = both[1].split(" ")

player_a_score = 0
player_b_score = 0

for x in range(0,len(player_a)):
	if(player_a[x] == "rock" and player_b[x] == "scissors"):
		print("player_a won! Rock beats scissors!")
		player_a_score+=1