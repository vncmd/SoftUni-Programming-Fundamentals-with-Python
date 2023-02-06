def get_even_odd(str_digit):
    even = 0
    odd = 0
    for digit_str in str_digit:
        digit = int(digit_str)
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit

    return [even, odd]


numbers = input()
result = get_even_odd(numbers)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")




