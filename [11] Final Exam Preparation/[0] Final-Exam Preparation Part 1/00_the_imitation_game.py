decrypted_message = input()

input_data = input()

while input_data != "Decode":
    data_split = input_data.split("|")
    command = data_split[0]

    if command == "Move":
        n_letters = int(data_split[1])
        first_part = decrypted_message[:n_letters]
        second_part = decrypted_message[n_letters:]
        decrypted_message = second_part + first_part
    elif command == "Insert":
        index = int(data_split[1])
        additional_string = data_split[2]

        decrypted_message = decrypted_message[:index] + additional_string + decrypted_message[index:]
    elif command == "ChangeAll":
        sub_string = data_split[1]
        replacement_string = data_split[2]
        decrypted_message = decrypted_message.replace(sub_string, replacement_string)

    input_data = input()

print(f"The decrypted message is: {decrypted_message}")