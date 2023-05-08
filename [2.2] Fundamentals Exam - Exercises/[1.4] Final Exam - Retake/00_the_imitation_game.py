def change_all(first_letter, second_letter):
    global main_string
    main_string = main_string.replace(first_letter, second_letter)


def insert_test(num, symbol):
    global main_string
    main_string = main_string[:num] + symbol + main_string[num:]


def move_string(num):
    global main_string
    main_string = main_string[num:] + main_string[:num]


main_string = input()
command = input()


while command != "Decode":
    command = command.split("|")
    decode_command = command[0]

    if decode_command == "ChangeAll":
        letter_one = command[1]
        letter_two = command[-1]
        change_all(letter_one, letter_two)

    elif decode_command == "Insert":
        number = int(command[1])
        symbol = command[-1]
        insert_test(number, symbol)

    elif decode_command == "Move":
        number = int(command[1])
        move_string(number)

    command = input()

print(f"The decrypted message is: {main_string}")
