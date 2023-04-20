import re

bought_furniture = []
total_money = 0

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

command_line = input()

while command_line != "Purchase":

    match = re.search(pattern, command_line)

    if match:

        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

    command_line = input()


print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
