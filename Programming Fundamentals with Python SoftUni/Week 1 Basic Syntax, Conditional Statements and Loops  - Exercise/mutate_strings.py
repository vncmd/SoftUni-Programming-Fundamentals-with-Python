first_str = input()
second_str = input()

last_printed = first_str
for chr_i in range(len(first_str)):
    left_part = second_str[:chr_i + 1]
    right_part = first_str[chr_i + 1:]
    current_str = left_part + right_part
    if current_str == last_printed:
        continue
    print(current_str)
    last_printed = current_str

