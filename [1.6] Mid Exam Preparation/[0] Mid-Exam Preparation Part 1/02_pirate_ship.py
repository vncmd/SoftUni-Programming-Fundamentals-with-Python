def is_valid_idx(idx, seq):
    return 0 <= idx < len(seq)


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

is_running = True
while is_running:
    line = input()
    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid_idx(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")
            break
    if command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid_idx(start_idx, pirate_ship) or not is_valid_idx(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break
    if command == "Repair":
        idx = int(command_args[1])
        health = int(command_args[2])
        if not is_valid_idx(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)
    if command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1

        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
