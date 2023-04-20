def is_idx_in_range(idx, cards_count):
    if 0 <= idx < cards_count:
        return True
    return False


def check_idx_validity(idx1, idx2, count_cards):
    if is_idx_in_range(idx1, count_cards) \
            and is_idx_in_range(idx2, count_cards) \
            and idx1 != idx2:
        return True
    return False


cards = input().split()

command = input()
n_moves = 0

while command != "end":
    n_moves += 1
    idx1, idx2 = [int(el) for el in command.split()]
    if check_idxs_validity(idx1, idx2, len(cards)):
        if cards[idx1] == cards[idx2]:
            element = cards[idx1]
            cards.pop(idx1)
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        element_to_add = f"-{n_moves}a"
        idx = len(cards) // 2
        cards.insert(idx, element_to_add)
        cards.insert(idx, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    if not cards:
        print(f"You have won in {n_moves} turns!")
        break

    command = input()

print(f"Sorry you lose :(")
print(*cards, sep=' ')