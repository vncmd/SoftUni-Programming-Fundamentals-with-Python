data = input()

cities = {}

while data != "Sail":
    data_split = data.split("||")
    city = data_split[0]
    population = int(data_split[1])
    gold = int(data_split[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}

    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    data = input()

data = input()

while data != "End":
    data_split = data.split("=>")
    command = data_split[0]
    city = data_split[1]

    if command == "Plunder":
        people = int(data_split[2])
        gold = int(data_split[3])

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(data_split[2])
        if gold >= 0:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

        else:
            print("Gold added cannot be a negative number!")

    data = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    for city, values in cities.items():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")