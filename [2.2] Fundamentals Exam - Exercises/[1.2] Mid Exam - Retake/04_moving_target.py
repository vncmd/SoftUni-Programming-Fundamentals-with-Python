def shoot(position, strike_damage):
    if 0 <= position < len(targets):
        targets[position] -= strike_damage

        if targets[position] <= 0:
            targets.pop(position)


def add_item(position, target_value):
    if 0 <= position < len(targets):
        targets.insert(position, target_value)

    elif position >= len(targets) or position < 0:
        print("Invalid placement!")


def strike(position, radius_strike):
    current_position_to_0 = position - radius_strike
    current_position_to_len_targets = position + radius_strike

    if current_position_to_0 >= 0 and current_position_to_len_targets < len(targets):
        del targets[current_position_to_0:current_position_to_len_targets + 1]

    elif current_position_to_0 < 0 or current_position_to_len_targets >= len(targets):
        print("Strike missed!")


targets = [int(target) for target in input().split()]
command = input()

while command != "End":
    command = command.split()
    event = command[0]
    idx = int(command[1])

    if event == "Shoot":
        strike_power = int(command[2])
        shoot(idx, strike_power)

    elif event == "Add":
        new_target = int(command[2])
        add_item(idx, new_target)

    elif event == "Strike":
        radius_of_strike = int(command[2])
        strike(idx, radius_of_strike)

    command = input()

print(*targets, sep="|")


# Different solution:

# targets = [int(x) for x in input().split()]
# data = input()
#
# while data != "End":
#     command, idx, value = [int(x) if x[-1].isdigit() else x for x in data.split()]
#     valid_idx = True
#     if not 0 <= idx < len(targets):
#         valid_idx = False
#
#     elif command == "Shoot":
#         targets[idx] -= value
#         if targets[idx] <= 0:
#             del targets[idx]
#
#     if command == "Add":
#         if valid_idx:
#             targets.insert(idx, value)
#         else:
#             print("Invalid placement!")
#
#     elif command == "Strike" and valid_idx:
#         start_radius = idx - value
#         end_radius = idx + value + 1
#         if 0 <= start_radius < end_radius < len(targets):
#             del targets[start_radius:end_radius]
#         else:
#             print("Strike missed!")
#
#     data = input()
#
# print(*targets, sep="|")
