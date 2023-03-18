text = input()

final_text = ""
last_letter = ""

for current_letter in text:
    if current_letter != last_letter:
        final_text += current_letter
        last_letter = current_letter

print(final_text)