import re

participants = {name.replace(" ", ""): 0 for name in input().split(",")}
racer_code = input()

letters_d = re.compile(r"([A-Za-z])")
numbers_d = re.compile(r"([0-9])")

while racer_code != "end of race":
    find_name = "".join(re.findall(letters_d, racer_code))
    find_nums = sum(int(num) for num in re.findall(numbers_d, racer_code))

    if find_name in participants.keys():
        participants[find_name] += find_nums

    racer_code = input()

participants = sorted(participants.items(), key=lambda x: -x[1])

print(f"1st place: {participants[0][0]}")
print(f"2nd place: {participants[1][0]}")
print(f"3rd place: {participants[2][0]}")
