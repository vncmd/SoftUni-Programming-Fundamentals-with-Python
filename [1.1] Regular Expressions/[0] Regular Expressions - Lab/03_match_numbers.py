import re

pattern = r"(^|(?<=\s))-?([0-9]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

text = input()

results = re.finditer(pattern, text)

for res in results:
    print(res.group(), end=" ")