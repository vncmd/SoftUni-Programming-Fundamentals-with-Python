to_do_list = [0] * 10

command = input()

while command != "End":
    order, task = command.split("-")
    order = int(order)
    index = order - 1
    to_do_list[index] = task
    command = input()

result = [task for task in to_do_list if task != 0]
print(result)

