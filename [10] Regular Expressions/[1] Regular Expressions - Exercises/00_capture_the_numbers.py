import re

pattern = r'\d+'

input_text = input()

while input_text:
    matches = re.findall(pattern, input_text)

    if matches:
        print(' '.join(matches), end=" ")

    input_text = input()
