rooms = input().split("|")


MAX_HEALTH = 100
health = MAX_HEALTH
bitcoins = 0
room_num = 0


for room in rooms:
    room_num += 1
    command, amount = room.split()
    amount = int(amount)

    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_num}")
            exit(0)

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")