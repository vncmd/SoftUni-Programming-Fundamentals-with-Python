cards = input().split()
shuffles = int(input())

first_half = []
second_half = []
for idx in range(shuffles):
    card = cards [idx]
    if idx < len(cards) / 2:
        first_half.append(card)
    else:
        second_half.append(card)

