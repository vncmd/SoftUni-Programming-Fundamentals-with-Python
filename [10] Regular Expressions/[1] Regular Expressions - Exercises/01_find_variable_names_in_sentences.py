import re

input_text = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

found_names = re.findall(pattern, input_text)

print(','.join(found_names))


# Different solution:
#
# import re
#
# input_string = input()
#
# pattern = re.compile(r"\b_(?P<word>[A-Za-z0-9]+\b)")
# result = re.finditer(pattern, input_string)
# match_list = []
# for show in result:
#     match_list.append(show["word"])
#
# print(','.join(match_list))