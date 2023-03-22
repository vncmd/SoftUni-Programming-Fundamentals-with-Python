import re

input_text = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

found_names = re.findall(pattern, input_text)

print(','.join(found_names))