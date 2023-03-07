products = {}

data = input().split()

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

searched_products = input().split()

for searched_product in searched_products:
    if searched_product in products.keys():
        print(f"We have {products[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")