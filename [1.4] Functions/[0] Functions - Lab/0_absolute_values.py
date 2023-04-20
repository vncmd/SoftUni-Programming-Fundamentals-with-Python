numbers_as_str = input().split()
numbers = []

for num_as_str in numbers_as_str:
    numbers.append(abs(float(num_as_str)))

print(numbers)
