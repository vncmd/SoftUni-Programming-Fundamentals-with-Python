def winning_valid(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']

    left_part = ticket[:10]
    right_part = ticket[10:]

    for match_symbol in winning_symbols:

        for uninterrupted_matches in range(10, 5, -1):
            win_symbols_reps = match_symbol * uninterrupted_matches

            if win_symbols_reps in left_part and win_symbols_reps in right_part:

                if uninterrupted_matches == 10:

                    return f'ticket "{ticket}" - {uninterrupted_matches}{match_symbol} Jackpot!'

                return f'ticket "{ticket}" - {uninterrupted_matches}{match_symbol}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    print(winning_valid(ticket))