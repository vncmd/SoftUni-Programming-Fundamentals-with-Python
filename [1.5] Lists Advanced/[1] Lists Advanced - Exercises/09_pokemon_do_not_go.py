distance = [int(x) for x in input().split()]

result = []

while distance:
    index = int(input())
    caught_pokemon = ""
    if index < 0:
        caught_pokemon = distance.pop(0)
        distance.insert(0, distance[-1])
    elif index >= len(distance):
        caught_pokemon = distance.pop(-1)
        distance.append(distance[0])
    if not caught_pokemon:
        caught_pokemon = distance.pop(index)
    result.append(caught_pokemon)
    for idx, pokemon in enumerate(distance):
        if pokemon <= caught_pokemon:
            distance[idx] += caught_pokemon
        else:
            distance[idx] -= caught_pokemon

print(sum(result))