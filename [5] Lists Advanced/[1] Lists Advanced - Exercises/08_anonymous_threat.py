def merge(start, end):
    if start < 0:
        start = 0
    if start < end:
        length = len(main_str)
        if end >= length:
            end = length - 1
        for num in range(start, end):
            main_str[start] += f"{main_str.pop(start + 1)}"


def divide(idx, partitions):
    length = len(main_str[idx])
    space_between = length // partitions
    string_to_change = main_str.pop(idx)
    result_ = []
    for x in range(partitions - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        main_str.insert(idx, x)


main_str = input().split()
commands = input()

while commands != "3:1":
    command, start_index, end_index = [int(x) if x[-1].isdigit() else x for x in commands.split()]
    if command == "merge":
        merge(start_index, end_index)
    elif command == "divide":
        divide(start_index, end_index)
    commands = input()

print(" ".join(main_str))