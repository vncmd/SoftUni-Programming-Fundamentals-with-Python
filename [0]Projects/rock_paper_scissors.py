import random
rock = "Rock"
paper = "paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]paper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_num = random.randint(1, 3)

computer_move = ""
if computer_random_num == 1:
    computer_move = rock
elif computer_move == 2:
    computer_move = paper
else:
    computer_move = scissors
    

