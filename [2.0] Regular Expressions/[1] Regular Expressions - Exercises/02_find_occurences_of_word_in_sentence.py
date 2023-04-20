import re

sentence = input()
searched_word = input()

pattern = fr'\b{searched_word}\b'

matches = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(len(matches))
