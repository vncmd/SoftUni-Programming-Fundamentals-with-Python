words = input().split()

count_by_letter = {}

for word in words:
    for letter in word:
        if letter in count_by_letter:
            count_by_letter[letter] += 1
        else:
            count_by_letter[letter] = 1

for letter, count in count_by_letter.items():
    print(f"{letter} -> {count}")