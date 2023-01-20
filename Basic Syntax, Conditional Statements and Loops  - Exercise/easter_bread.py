budget = float(input())
flour_price_kg = float(input())
breads_counter = 0
colored_eggs_counter = 0
eggs_price = flour_price_kg * 0.75
milk_price = flour_price_kg * 1.25 / 4
bread_price_unit = eggs_price + flour_price_kg + milk_price

while budget >= bread_price_unit:
    budget -= bread_price_unit
    breads_counter += 1
    colored_eggs_counter += 3
    if breads_counter % 3 == 0:
        colored_eggs_counter -= breads_counter - 2
print(f"You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}"
      f"BGN left.")

