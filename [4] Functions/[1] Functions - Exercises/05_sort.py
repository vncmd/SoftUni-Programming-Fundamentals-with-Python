def sorted_nums(numbers):
    numbers.sort()
    for n in numbers:
        nums_list.append(n)
    return nums_list


nums_list = []
nums = [int(x) for x in input().split()]

print(sorted(nums))