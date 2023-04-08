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
first_team_sent_off = initial_players - len(first_team_sent_off)
second_team_sent_off = initial_players - len(second_team_sent_off)

print(f"Team A - {first_team_sent_off}; Team B - {second_team_sent_off}")

if flag:
    print("Game was terminated")

# Different solution:
players = input().split()

first_team = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
second_team = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

terminated = False
for player in players:
    if player in first_team:
        first_team.remove(player)
    elif player in second_team:
        second_team.remove(player)
    if len(first_team) < 7 or len(second_team) < 7:
        terminated = True
        break

print(f"Team A - {len(first_team)}; Team B - {len(second_team)}")

if terminated:
    print("Game was terminated")