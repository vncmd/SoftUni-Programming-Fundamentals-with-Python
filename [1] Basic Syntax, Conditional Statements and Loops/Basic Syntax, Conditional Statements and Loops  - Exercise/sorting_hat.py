name = input()
house = 0
character = 0
while name != "Welcome!":
    name = name
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    character = len(name)

    if character < 5:
        house = f"{name} goes to Gryffindor."
    elif character == 5:
        house = f"{name} goes to Slytherin."
    elif character == 6:
        house = f"{name} goes to Ravenclaw."
    elif character > 6:
        house = f"{name} goes to Hufflepuff."
    print(house)
    name = input()
else:
    print("Welcome to Hogwarts.")