events = input().split("|")
total_coins = 100
total_energy = 100
open_factory = True

for event in events:
    event_items = event.split("-")
    type_event = event_items[0]
    event_value = int(event_items[1])
    if type_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_event}")
        else:
            print(f"Closed! Cannot afford {type_event}.")
            open_factory = False
            break

if open_factory:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")