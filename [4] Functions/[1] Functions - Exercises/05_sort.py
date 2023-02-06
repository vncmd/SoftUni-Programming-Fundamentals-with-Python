def sorted_nums(numbers):
    numbers.sort()
    for n in numbers:
        sort_list.append(n)
    return sort_list


nums_list = []
nums = [int(x) for x in input().split()]

print(sorted(nums))
