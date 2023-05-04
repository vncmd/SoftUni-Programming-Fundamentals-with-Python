people = int(input())
current_wagons = [int(x) for x in input().split()]

for idx in range(len(current_wagons)):
    max_people = min(4 - current_wagons[idx], people)
    current_wagons[idx] += max_people
    people -= max_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif any([wagon < 4 for wagon in current_wagons]):
    print("The lift has empty spots!")

print(*current_wagons)
