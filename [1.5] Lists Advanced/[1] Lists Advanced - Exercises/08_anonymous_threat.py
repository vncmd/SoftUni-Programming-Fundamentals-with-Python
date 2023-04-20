def merge(start, end):
    if start < 0:
        start = 0
    if start < end:
        length = len(words)
        if end >= length:
            end = length - 1
        for num in range(start, end):
            words[start] += f"{words.pop(start + 1)}"


def divide(idx, partitions):
    length = len(words[idx])
    partition_size = length // partitions
    string_to_change = words.pop(idx)
    result = []
    for x in range(partitions - 1):
        result.append(string_to_change[:partition_size])
        string_to_change = string_to_change[partition_size:]
    result.append(string_to_change)
    for x in result[::-1]:
        words.insert(idx, x)


words = input().split()
line = input()
while line != "3:1":
    command, start_index, end_index = [int(x) if x[-1].isdigit() else x for x in line.split()]
    if command == "merge":
        merge(start_index, end_index)
    elif command == "divide":
        divide(start_index, end_index)
    line = input()

print(" ".join(words))