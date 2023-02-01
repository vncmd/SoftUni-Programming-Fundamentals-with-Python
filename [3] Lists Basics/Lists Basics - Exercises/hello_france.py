items_accessories = input().split("|")
budget = int(input())

items_price = []
selling_items = []
budget_left = budget
train_ticket = 150

for idx in items_accessories:
    if "Clothes->" in idx:
        text = float(idx.replace("Clothes->", ""))

        if 0 < text <= 50 and budget_left >= text:
            items_price.append(text)
            budget_left -= text
            selling_items.append(text + text * 0.40)

    elif "Shoes->" in idx:
        text = float(idx.replace("Shoes->", ""))

        if 0 < text <= 35 and budget_left >= text:
            items_price.append(text)
            budget_left -= text
            selling_items.append(text + text * 0.40)

    elif "Accessories->" in idx:
        text = float(idx.replace("Accessories->", ""))

        if 0 < text < 20.50 and budget_left >= text:
            items_price.append(text)
            budget_left -= text
            selling_items.append(text + text * 0.40)

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