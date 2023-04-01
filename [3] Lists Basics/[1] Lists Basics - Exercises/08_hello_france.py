items_accessories = input().split("|")
budget = int(input())

items_price = []
budget_left = budget
selling_items = []
train_ticket = 150

for item in items_accessories:
    if "Clothes->" in item:
        item_price = float(item.replace("Clothes->", ""))

        if 0 < item_price <= 50 and budget_left >= item_price:
            items_price.append(item_price)
            budget_left -= item_price
            selling_items.append(item_price + item_price * 0.40)

    elif "Shoes->" in item:
        item_price = float(item.replace("Shoes->", ""))

        if 0 < item_price <= 35 and budget_left >= item_price:
            items_price.append(item_price)
            budget_left -= item_price
            selling_items.append(item_price + item_price * 0.40)

    elif "Accessories->" in item:
        item_price = float(item.replace("Accessories->", ""))

        if 0 < item_price < 20.50 and budget_left >= item_price:
            items_price.append(item_price)
            budget_left -= item_price
            selling_items.append(item_price + item_price * 0.40)

for n in selling_items:
    print(f"{n:.2f}", end=" ")

normal_price = sum(items_price)
re_sale = sum(selling_items)
difference = re_sale - normal_price

print(f"\nProfit: {difference:.2f}")

if budget + difference > train_ticket:
    print(f"Hello, France!")
else:
    print("Not enough money.")