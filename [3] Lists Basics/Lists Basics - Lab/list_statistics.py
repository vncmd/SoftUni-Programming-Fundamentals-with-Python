n = int(input())

positive_numbers = []
negative_numbers = []

for i in range(n):
    current_num = int(input())
    if current_num >= 0:
        positive_numbers.append(current_num)
    else:
        negative_numbers.append(current_num)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")

