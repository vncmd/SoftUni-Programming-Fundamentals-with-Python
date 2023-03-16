sequence = input().split()

new_sequence = ""

for word in range(len(sequence)):
    counter = len(sequence)
    for repeat in range(counter):
        new_sequence += sequence[word]

print(new_sequence)