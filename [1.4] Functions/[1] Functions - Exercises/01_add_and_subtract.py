def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

addition = add(first, second)
result = subtract(addition, third)

print(result)