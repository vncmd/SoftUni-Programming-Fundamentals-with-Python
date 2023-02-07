def is_perfect(nums):
    total_sum = 0
    for divisor in range(1, nums):
        if nums % divisor == 0:
            total_sum += divisor
    if total_sum == nums:
        return first_cond
    return second_cond


first_cond = f"We have a perfect number!"
second_cond = f"It's not so perfect."

number = int(input())
print(is_perfect(number))