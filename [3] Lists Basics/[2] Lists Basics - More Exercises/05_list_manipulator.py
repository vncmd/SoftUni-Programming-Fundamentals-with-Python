data = [int(num) for num in input().split()]
manipulations = input().split()

while manipulations[0] != "end":
    even = [num for num in data if num % 2 == 0]
    odd = [num for num in data if num % 2 != 0]

    if manipulations[0] == "exchange":
        if 0 <= int(manipulations[1]) < len(data):
            data = data[int(manipulations[1]) + 1:] + data[:int(manipulations[1]) + 1]
        else:
            print(f'Invalid index')

    elif manipulations[0] == "max":
        if manipulations[1] == "even" and even:
            print((len(data) - data[::-1].index(max(even)) - 1))
        elif manipulations[1] == "odd" and odd:
            print((len(data) - data[::-1].index(max(odd)) - 1))
        else:
            print('No matches')

    elif manipulations[0] == "min":
        if manipulations[1] == "even" and even:
            print((len(data) - data[::-1].index(min(even)) - 1))
        elif manipulations[1] == "odd" and odd:
            print((len(data) - data[::-1].index(min(odd)) - 1))
        else:
            print('No matches')

    elif manipulations[0] == "first":
        if 0 < int(manipulations[1]) <= len(data):
            if manipulations[2] == "even":
                print(even[0:int(manipulations[1])])
            else:
                print(odd[0:int(manipulations[1])])
        else:
            print(f"Invalid count")

    elif manipulations[0] == "last":
        if 0 < int(manipulations[1]) <= len(data):
            if manipulations[2] == "even":
                print(even[-int(manipulations[1]):])
            else:
                print(odd[-int(manipulations[1]):])
        else:
            print(f"Invalid count")

    manipulations = input().split()

print(data)