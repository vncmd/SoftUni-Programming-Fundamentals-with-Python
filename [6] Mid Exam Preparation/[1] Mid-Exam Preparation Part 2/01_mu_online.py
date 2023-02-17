rooms = input().split("|")

MAX_HEALTH = 100
health = MAX_HEALTH
bitcoins = 0

room_number = 0

for room in rooms:
    room_number += 1
    command, amount = room.split()
    # Try with floats if errors
    amount = int(amount)

    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH