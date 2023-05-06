tour = input()
command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        idx, string = int(command[1]), command[2]
        if idx < len(tour):
            tour = tour[0:idx] + string + tour[idx:]

    elif action == "Remove Stop":
        start_idx, end_idx = int(command[1]), int(command[2])
        if end_idx < len(tour) and start_idx < len(tour):
            tour = tour[0:start_idx] + tour[end_idx + 1:]
    elif action == "Switch":
        old_str, new_str = command[1], command[2]

        if old_str in tour:
            tour = tour.replace(old_str, new_str)

    print(tour)

    command = input()

print(f"Ready for world tour! Planned stops: {tour}")
