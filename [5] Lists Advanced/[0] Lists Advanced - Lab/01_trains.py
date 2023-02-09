n_wagons = int(input())
train = [0] * n_wagons

commands = input()

while commands != "End":
    split_data = commands.split()
    action = split_data[0]
    if commands.startswith("add"):
        n_people = int(split_data[1])
        train[-1] += n_people
    elif action == "insert":
        index = int(split_data[1])
        n_people = int(split_data[2])
        train[index] += n_people
    elif action == "leave":
        index = int(split_data[1])
        n_people = int(split_data[2])
        train[index] -= n_people
    commands = input()

print(train)