def min_num():
    result_min = min(numbers)
    return result_min


def max_num():
    result_max = max(numbers)
    return result_max


def sum_num():
    result_sum = sum(numbers)
    return result_sum


numbers = [int(n) for n in input().split()]

result = [min_num(), max_num(), sum_num()]

print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result[2]}")