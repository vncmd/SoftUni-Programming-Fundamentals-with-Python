text = input()

letter_position = []

for position, letter in enumerate(text):
    if letter.isupper():
        letter_position.append(position)


print(letter_position)
