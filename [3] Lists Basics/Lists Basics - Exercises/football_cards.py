cards = input().split()

first_team_sent_off = 0
second_team_sent_off = 0
for card in cards:
    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == "A"
    if is_first_team:
        first_team_sent_off += 1
    else:
        second_team_sent_off += 1


