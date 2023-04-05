permutations = [int(number) for number in input().split()]

kills = int(input())
counter = 0
numbers = []
index = 0

while len(permutations) > 0:
    counter += 1
    if counter % kills == 0:
        numbers.append(permutations[index])
        permutations.pop(index)
    elif counter % kills != 0:
        index += 1

    if index >= len(permutations):
        index = 0


print(str(numbers).replace(' ', ''))


