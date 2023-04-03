first_string = input()
second_string = input()

last_printed = first_string
for chr_i in range(len(first_string)):

    left_part = second_string[:chr_i]
    right_part = first_string[chr_i:]
    current_str = left_part + right_part
    if current_str == last_printed:
        continue
    print(current_str)
    last_printed = current_str

