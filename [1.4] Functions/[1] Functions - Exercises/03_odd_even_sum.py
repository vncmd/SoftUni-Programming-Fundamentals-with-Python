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


# Different solution:

# def even_odd_nums(number):
#     odd_sum = 0
#     even_sum = 0
#     for digit in number:
#         if int(digit) % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#     return odd_sum, even_sum
#
#
# numbers = input()
#
# odd_digits, even_digits = even_odd_nums(numbers)
# print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")
