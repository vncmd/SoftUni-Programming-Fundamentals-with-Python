cards = input().split()

flag = False

first_team_sent_off = []
second_team_sent_off = []
for card in cards:
    if card in first_team_sent_off or card in second_team_sent_off:
        continue
    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == "A"
    if is_first_team:
        first_team_sent_off.append(card)
    else:
        second_team_sent_off.append(card)

    if len(first_team_sent_off) > 4 or len(second_team_sent_off) > 4:
        flag = True
        break

initial_players = 11
first_team_players = initial_players - len(first_team_sent_off)
second_team_sent_off = initial_players - len(second_team_sent_off)

print(f"Team A - {first_team_players}; Team B - {second_team_sent_off}")

if flag:
    print("Game was terminated")