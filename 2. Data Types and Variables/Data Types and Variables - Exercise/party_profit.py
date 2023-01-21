people = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        people -= 2
    if day % 15 == 0:
        people += 5
    if day % 3 == 0:
        coins -= 3 * people
    if day % 5 == 0:
        coins += 20 * people
        if day % 3 == 0:
            coins -= 2 * people
    coins += 50
    coins -= 2 * people

coins_per_person = int(coins // people)
print(f"{people} companions received {coins_per_person} coins each.")
