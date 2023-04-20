def tribonacci(num):
    last_three = [1, 1]
    for number in range(1, num + 1):

        if number == 1 or number == 2:
            print(last_three[number - 1], end=" ")
            continue

        else:
            add_last_number = 0

            if len(last_three) > 2:
                add_last_number = last_three.pop(0)

        print(sum(last_three) + add_last_number, end=" ")
        last_three.append(sum(last_three) + add_last_number)


starting_number = int(input())

tribonacci(starting_number)
