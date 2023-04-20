def calculate(command, first_num, second_num):
    result = 0
    if command == "multiply":
        result = first_num * second_num
    elif command == "divide":
        result = int(first_num / second_num)
    elif command == "add":
        result = first_num + second_num
    else:
        result = first_num - second_num

    return result


command_operator = input()
num_1 = int(input())
num_2 = int(input())

res = calculate(command_operator, num_1, num_2)
print(res)