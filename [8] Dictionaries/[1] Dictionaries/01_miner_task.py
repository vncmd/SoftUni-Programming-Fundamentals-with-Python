resources = {}

while True:
    current_resource = input()

    if current_resource == "stop":
        break

    current_quantity = int(input())

    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += current_quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")