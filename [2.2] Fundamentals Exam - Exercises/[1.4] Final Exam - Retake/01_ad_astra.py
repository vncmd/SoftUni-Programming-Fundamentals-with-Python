import re

main_string = input()

patterns = re.compile(
    r"([|#])(?P<item_name>[A-Za-z ]+)\1(?P<epx_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]+)\1")

result_info = {}
result = re.finditer(patterns, main_string)
total = 0

for data in result:
    total += int(data["calories"])

    result_info[data["item_name"]] = {}
    result_info[data["item_name"]]["date"] = data["exp_date"]
    result_info[data["item_name"]]["nutrition"] = data["calories"]

total = int(total / 2000)

print(f"You have food to last you for: {total} days!")

for name in result_info:
    print(f"Item: {name}, Best before: {result_info[name]['date']}, Nutrition: {result_info[name]['nutrition']}")
