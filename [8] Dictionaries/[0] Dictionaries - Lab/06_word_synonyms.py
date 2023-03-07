count = int(input())
synonyms = {}

for _ in range(count):
    key = input()
    value = input()

    if key not in synonyms:
        synonyms[key] = []

    synonyms[key].append(value)

for word, all_synonyms in synonyms.items():
    print(f"{word} - {', '.join(all_synonyms)}")
