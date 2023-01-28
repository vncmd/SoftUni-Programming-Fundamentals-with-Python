factor = int(input())
boundary = int(input())

result = []

for num in range(1, boundary + 1):
    result.append(num * boundary)

print(result)