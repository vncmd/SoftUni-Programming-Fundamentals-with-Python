text = input()

wolf_check = text.split(", ")
number_check = len(wolf_check) - 1

printed_text = ""

for wolf in wolf_check:

    if wolf == "wolf" and number_check == 0:
        printed_text = "Please go away and stop eating my sheep"

    elif wolf == "wolf":
        printed_text = f"Oi! Sheep number {number_check}! You are about to be eaten by a wolf!"

    number_check -= 1

print(printed_text)