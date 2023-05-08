import re

number_products_to_scan = int(input())

default_barcode = "00"
group_d = "Product group:"
patterns = re.compile(r"@#+(?P<found_text>[A-Z][a-zA-Z0-9]{4,}[A-Z])@#+")

for _ in range(number_products_to_scan):
    bar_code = input()

    main_string = re.finditer(patterns, bar_code)
    found = False
    for a in main_string:
        found = True
        result = "".join(x for x in a["found_text"] if x.isdigit())

        if result:
            print(f"{group_d} {result}")
        else:
            print(f"{group_d} {default_barcode}")
    if not found:
        print("Invalid barcode")
