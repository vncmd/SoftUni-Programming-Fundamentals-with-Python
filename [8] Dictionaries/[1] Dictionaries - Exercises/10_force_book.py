force_side_tracker = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        command_args = command.split(" | ")
        force_side, force_user = command_args
        user_part_of_force = False

        for value in force_side_tracker.values():
            if force_user in value:
                user_part_of_force = True
                break

        if not user_part_of_force:
            if force_side not in force_side_tracker.keys():
                force_side_tracker[force_side] = [force_user]
            else:
                force_side_tracker[force_side].append(force_user)

    elif "->" in command:
        command_args = command.split(" -> ")
        force_user, force_side = command_args

        for key, value in force_side_tracker.items():
            if force_user in value:
                force_side_tracker[key].pop(value.index(force_user))
                break

        if force_side not in force_side_tracker.keys():
            force_side_tracker[force_side] = [force_user]

        else:
            force_side_tracker[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for force_side, force_users in force_side_tracker.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")

        for user in force_users:
            print(f"! {user}")