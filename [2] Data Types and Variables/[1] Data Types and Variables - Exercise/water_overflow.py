n_lines = int(input())

capacity = 255
tank = 0

for liters in range(n_lines):
    poured_lt = int(input())
    if tank + poured_lt > capacity:
        print(f"Insufficient capacity!")
    else:
        tank += poured_lt

print(tank)