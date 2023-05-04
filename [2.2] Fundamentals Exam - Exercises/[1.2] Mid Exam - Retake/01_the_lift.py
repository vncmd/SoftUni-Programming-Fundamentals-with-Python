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

# Different solution:

people = int(input())
max_people = 4
current = [int(num) for num in input().split()]

for el in range(len(current)):
    if people >= 4:
        if current[el] == 0:
            current[el] += 4
            people -= 4
        else:
            c_num = max_people - int(current[el])
            current[el] += c_num
            people -= c_num
    else:
        current[el] += people
        people = 0

check_nums = [int(num) for num in current if num != 4]

if people == 0 and check_nums:
    print("The lift has empty spots!")
    print(*current, sep=" ")
if people != 0 and not check_nums:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*current, sep=" ")
if people == 0 and not check_nums:
    print(*current, sep=" ")
