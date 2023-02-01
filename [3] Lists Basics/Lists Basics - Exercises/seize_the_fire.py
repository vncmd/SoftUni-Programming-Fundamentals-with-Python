cells = input().split("#")
water = int(input())

seized_cells = []
total_fire = 0
for cell in cells:
    cell_args = cell.split(" = ")
    level = cell_args[0]
    value = int(cell_args[1])

    if level == "High" and (value < 81 or value > 125):
        continue

    if level == "Medium" and (value < 51 or value > 80):
        continue

    if level == "Low" and (value < 1 or value > 50):
        continue

    if value > water:
        continue

    water -= value
    total_fire += value
    seized_cells.append(value)

print(f"Cells:")
for cell in seized_cells:
    print(f" - {cell}")

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")

print(f"Total Fire: {total_fire}")