numbers_str = input().split(", ")

counter = 0
numbers = []
numbers_to_delete = []

for num in range(len(numbers_str)):
    int_num = int(numbers_str[num])
    numbers.append(int_num)

for num in range(len(numbers)):
    numbers_to_delete.append(numbers[num])

for num in range(len(numbers)):
    if numbers[num] == 0:
        numbers_to_delete.remove(0)
        counter += 1

for zero in range(1, counter + 1):
    numbers_to_delete.append(0)

print(numbers_to_delete)