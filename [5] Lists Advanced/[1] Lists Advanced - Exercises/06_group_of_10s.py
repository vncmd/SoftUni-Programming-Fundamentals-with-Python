from math import ceil
numbers = [int(x) for x in input().split(", ")]

low_boundary = 1
high_boundary = 10
group_max = ceil((max(numbers) / 10))
for idx in range(1, group_max + 1):
    grouped_nums = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {10 * idx}'s: {grouped_nums}")

    low_boundary += 10
    high_boundary += 10


