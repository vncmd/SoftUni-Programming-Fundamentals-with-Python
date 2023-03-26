def is_valid_idx(index, seq):
    return 0 <= index < len(seq)


text = input()
while True:
    line = input()
    if line == "Travel":
        break

    command_args = line.split(":")
    command = command_args[0]

    if command == "Add Stop":
        idx = int(command_args[1])
        new_stop = command_args[2]

        if is_valid_idx(idx, text):
            text = text[:idx] + new_stop + text[idx:]
    elif command == "Remove Stop":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])

        if is_valid_idx(start_idx, text) and is_valid_idx(end_idx, text):
            text = text[:start_idx] + text[end_idx + 1:]

    else:
        old_str = command_args[1]
        new_str = command_args[2]
        text = text.replace(old_str, new_str)

    print(text)

print(f"Ready for world tour! Planned stops: {text}")
