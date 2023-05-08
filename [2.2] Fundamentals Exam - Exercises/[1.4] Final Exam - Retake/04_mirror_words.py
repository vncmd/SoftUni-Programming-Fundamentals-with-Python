import re

main_str = input()

patterns = re.compile(r"([@#])(?P<word>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1")
result_list = []

result = list(re.finditer(patterns, main_str))

for show in result:
    if show["word"] == show["word2"][::-1]:
        result_list.append(f"{show['word']} <=> {show['word2']}")

if result:
    print(f"{len(result)} word pairs found!")

    if result_list:
        print("The mirror words are:")
        print(*result_list, sep=", ")
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
