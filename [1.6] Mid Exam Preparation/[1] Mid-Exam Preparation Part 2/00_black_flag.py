days = int(input())
daily = int(input())
expected = float(input())


total = 0
for day in range(1, days + 1):
    total += daily

    if day % 3 == 0:
        total += daily * 0.5

    if day % 5 == 0:
        total -= total * 0.3

if total >= expected:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = total / expected * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")