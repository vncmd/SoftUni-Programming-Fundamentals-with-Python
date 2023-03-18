text = input()

all_text = ''
current = ''

for char in range(len(text)):

    if char + 1 < len(text) and text[char].isdigit() and text[char + 1].isdigit():
        current = current * int(text[char:char + 2])
        all_text += current
        current = ''

    elif text[char].isdigit():
        current = current * int(text[char])
        all_text += current
        current = ''

    else:
        current += text[char]

all_text = all_text.upper()
letter_check = ''

for letter in all_text:
    if letter not in letter_check:
        letter_check += letter


print(f"Unique symbols used: {len(letter_check)}")
print(all_text)