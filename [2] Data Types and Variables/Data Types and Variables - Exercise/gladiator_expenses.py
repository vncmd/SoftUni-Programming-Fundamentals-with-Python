lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broken = 0
cost = 0

for day in range(1, lost_fights + 1):
    if day % 2 == 0:
        cost += helmet_price
    if day % 3 == 0:
        cost += sword_price
    if day % 2 == 0 and day % 3 == 0:
        cost += shield_price
        shield_broken += 1
        if shield_broken % 2 == 0:
            cost += armor_price

print(f"Gladiator expenses: {cost:.2f} aureus")