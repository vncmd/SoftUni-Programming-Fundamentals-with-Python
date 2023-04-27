import re

income = 0
pattern = re.compile(
    r"(%)(?P<customer>[A-Z][a-z]+)\1([^\|\$\%\.]*)"
    
    r"<(?P<product>[\w]+)>([^\|\$\%\.]*)"
    
    r"\|(?P<count>[\d]+)\|([^\|\$\%\.]*)"
    
    r"(?P<price>[1-9]+[.0-9]*)\$"
)


data = input()

while data != "end of shift":
    result = re.finditer(pattern, data)

    for show in result:
        current_price = float(show["count"]) * float(show["price"])

        print(f"{show['customer']}: {show['product']} - {current_price:.2f}")

        income += current_price

    data = input()

print(f"Total income: {income:.2f}")
