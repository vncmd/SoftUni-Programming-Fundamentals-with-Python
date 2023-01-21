nums = int(input())

total_sum = 0

for i in range(nums):
    letter = input()
    total_sum += ord(letter)

    print(total_sum)
