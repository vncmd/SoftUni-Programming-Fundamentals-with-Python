from random import randint
from colorama import Fore

computer_num = randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print(f"{Fore.RED}Well that's an invalid input. You can try again.")
        continue

    player_number = int(player_input)

    if player_number == computer_num:
        print(f"{Fore.GREEN}Well, you guessed it!")

    elif player_number > computer_num:
        print(f"{Fore.LIGHTYELLOW_EX}That's... Too High!")

    else:
        print(f"{Fore.LIGHTYELLOW_EX}Nope... that's Too Low!")


