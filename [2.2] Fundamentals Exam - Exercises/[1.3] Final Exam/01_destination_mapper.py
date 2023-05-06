import re

main_str = input()
patterns = re.compile(
    r"([=/])(?P<location>[A-Z][a-zA-Z]{2,})\1"
)

list_result = []
result = re.finditer(patterns, main_str)
total_points = 0

for show in result:
    list_result.append(show["location"])
    total_points += len(show["location"])

print(f"Destinations: {', '.join(list_result)}")
print(f"Travel Points: {total_points}")
