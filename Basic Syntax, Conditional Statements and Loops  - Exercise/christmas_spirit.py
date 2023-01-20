quantity = int(input())
remaining_days = int(input())

budget = 0
spirit = 0
ornament = 2
skirt = 5
garlands = 3
lights = 15

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        budget += ornament * quantity
        spirit += 5
    if current_day % 3 == 0:
        budget += (skirt + garlands) * quantity
        spirit += 13
    if current_day % 5 == 0:
        budget += lights * quantity
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        budget += skirt + garlands + lights
if remaining_days % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")