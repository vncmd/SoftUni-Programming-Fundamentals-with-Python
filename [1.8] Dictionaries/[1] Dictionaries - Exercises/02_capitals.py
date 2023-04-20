countries = input().split(", ")
capitals = input().split(", ")
result = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in result.items():
    print(f"{country} -> {capital}")
