n = int(input())
word = input()

strings = []
special_word = []
for i in range(n):
    current_str = input()
    strings.append(current_str)

    if word in current_str:
        special_word.append(current_str)

print(strings)
print(special_word)
