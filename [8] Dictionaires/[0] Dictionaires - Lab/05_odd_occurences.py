words_keys = [el.lower() for el in input().split()]
default = 0

occurrences = dict.fromkeys(words_keys, default)
for word in words_keys:
    occurrences[word] = words_keys.count(word)

for word, count in occurrences.items():
    if count % 2 != 0:
        print(word, end=" ")

