def swap(idx_1, idx_2, list):
    list[idx_1], list[idx_2] = list[idx_2], list[idx_1]


def multiply(idx_1, idx_2, list):
    product = list[idx_1] * list[idx_2]
    list[idx_1] = product


def decrease(list):
    for el in range(len(list)):
        numbers[el] -= 1


numbers = [int(num) for num in input().split()]
command = input()

while command != "end":
    current_command = command.split()
    action = current_command[0]

    if action == "swap":
        idx1 = int(current_command[1])
        idx2 = int(current_command[2])
        swap(idx1, idx2, numbers)

    elif action == "multiply":
        idx1 = int(current_command[1])
        idx2 = int(current_command[2])
        multiply(idx1, idx2, numbers)

    elif action == "decrease":
        decrease(numbers)

    command = input()

str_numbers = list(map(lambda x: str(x), numbers))

print(", ".join(str_numbers))


# Different solution:

# elements = [int(x) for x in input().split()]
#
# data = input()
# while data != "end":
#     if "decrease" in data:
#         elements = [x - 1 for x in elements]
#
#         data = input()
#         continue
#
#     command, first_idx, second_idx = [x if x.isalpha() else int(x) for x in data.split()]
#
#     if command == "swap":
#         elements[first_idx], elements[second_idx] = elements[second_idx], elements[first_idx]
#
#     elif command == "multiply":
#         elements[first_idx] *= elements[second_idx]
#
#     data = input()
#
# print(*elements, sep=", ")
