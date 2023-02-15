def find_idx_by_element(seq, el):
    for el_idx in range(len(seq)):
        if seq[el_idx] == el:
            return el_idx

    return - 1


products = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break
    command_args = line.split()
    command = command_args[0]
    product = command_args[1]

    if command == "Urgent":
        if product not in products:
            products.insert(0, product)
    elif command == "Unnecessary":
        if product in products:
            products.remove(product)
    elif command == "Correct":
        new_product = command_args[2]
        idx = find_idx_by_element(products, product)
        if idx == - 1:
            continue
        products[idx] = new_product
    elif command == "Rearrange":
        if product in products:
            idx = find_idx_by_element(products, product)
            products.pop(idx)
            products.append(product)


print(", ".join(products))