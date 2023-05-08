main_msg = input()
command = input()

while command != "Reveal":
    command_type, *info = command.split(":|:")
    error_found = False

    if command_type == "ChangeAll":
        main_msg = main_msg.replace(info[0], info[1])

    elif command_type == "Reverse":
        substring = info[0]

        if substring not in main_msg:
            print("error")

            error_found = True
        else:
            main_msg = main_msg.replace(substring, "", 1) + substring[::-1]

    elif command_type == "InsertSpace":
        idx_to_insert = int(info[0])
        main_msg = main_msg[:idx_to_insert] + " " + main_msg[idx_to_insert:]

    if not error_found:
        print(main_msg)

    command = input()

print(f"You have a new text message: {main_msg}")
