main = [int(x) for x in input().split(", ")]
even = []

for num, index in enumerate(main):
    if index % 2 == 0:
        even.append(num)

print(even)