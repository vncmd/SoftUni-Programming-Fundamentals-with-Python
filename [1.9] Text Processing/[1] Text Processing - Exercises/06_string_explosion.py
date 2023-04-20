input_text = input()

new_text = ""
strength = 0

for idx in range(len(input_text)):
    if strength > 0 and input_text[idx] != ">":
        strength -= 1
    elif input_text[idx] == ">":
        new_text += input_text[idx]
        strength += int(input_text[idx + 1])
    else:
        new_text += input_text[idx]

print(new_text)