first_string = input()
second_string = input()

last_printed = first_string
for chr_i in range(len(first_string)):
    left_part = second_string[:chr_i + 1]
    right_part = first_string[chr_i + 1:]
    current_string = left_part + right_part
    if current_string == last_printed:
        continue
    print(current_string)
    last_printed = current_string

