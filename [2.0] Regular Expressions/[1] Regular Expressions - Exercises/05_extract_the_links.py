import re

valid_urls = []

pattern = r'(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'

input_line = input()

while input_line:
    matches = re.search(pattern, input_line)

    if matches:
        valid_urls.append(matches.group(0))

    input_line = input()

for valid_url in valid_urls:
    print(valid_url)