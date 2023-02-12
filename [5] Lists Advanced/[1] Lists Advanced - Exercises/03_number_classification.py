numbers = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f'Positive: {", ".join([str(x) for x in positive])}')
print(f'Negative: {", ".join([str(x) for x in negative])}')
print(f'Even: {", ".join([str(x) for x in even])}')
print(f'Odd: {", ".join([str(x) for x in odd])}')