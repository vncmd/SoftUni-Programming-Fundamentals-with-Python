import re

names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

valid_names = re.findall(pattern, names)

print(' '.join(valid_names))