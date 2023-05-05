starting_energy = int(input())
distance = input()
wins = 0

while distance != "End of battle":
    distance = int(distance)
    starting_energy -= distance

    if starting_energy < 0:
        print(f"Not enough energy! Game ends with {wins} won battles and {starting_energy + distance} energy")
        break

    wins += 1
    if wins % 3 == 0:
        starting_energy += wins

    distance = input()

else:
    print(f"Won battles: {wins}. Energy left: {starting_energy}")
