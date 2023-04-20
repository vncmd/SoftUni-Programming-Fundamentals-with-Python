def calculate_total(x_product, x_quantity):
    result = 0
    if product_buy == "water":
        result = req_quantity * 1
    elif product_buy == "coffee":
        result = req_quantity * 1.50
    elif product_buy == "coke":
        result = req_quantity * 1.40
    elif product_buy == "snacks":
        result = req_quantity * 2

    return result


product_buy = input()
req_quantity = int(input())
output = calculate_total(product_buy, req_quantity)
print(f"{output:.2f}")
