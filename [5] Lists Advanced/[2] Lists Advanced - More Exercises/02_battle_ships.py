def attack(all_attacks, attacks):
    destroyed_ships = 0
    for n_attack in range(len(attacks)):
        current_attack = attacks[attack]
        current_row, current_column = [int(num) for num in current_attack.split("-")]
        for n_row in range(len(all_attacks)):
            if n_row == current_row:
                now_row = all_attacks[current_row]
                if now_row[current_column] > 0:
                    now_row[current_column] -= 1
                    if now_row[current_column] == 0:
                        destroyed_ships += 1

    print(destroyed_ships)


rows = int(input())
all_ships = []

for x in range(rows):
    row = [int(num) for num in input().split()]
    all_ships.append(row)

n_attacks = input().split()
attack(all_ships, n_attacks)
