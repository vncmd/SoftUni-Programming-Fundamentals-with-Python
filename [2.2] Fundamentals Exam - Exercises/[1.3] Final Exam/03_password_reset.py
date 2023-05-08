def odd_chr(main_str):
    result = "".join(main_str[x] for x in range(len(main_str)) if x % 2 != 0)
    print(result)

    return result


def cut_string(index, length, main_str):
    result = main_str[:index] + main_str[index + length:]
    print(result)

    return result


def substitute_string(substring, substitute, main_str):
    if substring in main_str:
        result = main_str.replace(substring, substitute)
        print(result)

        return result

    print("Nothing to replace!")

    return main_str


main_string = input()
command = input()

while command != "Done":
    if "TakeOdd" in command:
        main_string = odd_chr(main_string)

        command = input()

        continue
    idx, index_or_substring, length_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]

    if "Cut" in command:
        main_string = cut_string(index_or_substring, length_or_substitute, main_string)

    elif "Substitute" in command:
        main_string = substitute_string(index_or_substring, length_or_substitute, main_string)

    command = input()


print(f"Your password is: {main_string}")
