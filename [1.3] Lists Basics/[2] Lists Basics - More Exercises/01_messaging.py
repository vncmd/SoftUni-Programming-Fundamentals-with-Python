numbers = [n for n in input().split()]
text = input()

message = ""
for num in numbers:
    find_index = sum([int(num_str) for num_str in num])
    if find_index >= len(text):
        find_index = find_index - len(text)
    message += text[find_index]
    text = text[:find_index] + text[find_index + 1:]

print(message)