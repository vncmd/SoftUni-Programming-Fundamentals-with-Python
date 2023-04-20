n_1 = [int(number) for number in input().split()]
n_2 = [int(number) for number in input().split()]
n_3 = [int(number) for number in input().split()]
first_win = False
second_win = False
draw = False


def game():
    global first_win, second_win, draw
    if (n_1[0] == 1 and n_2[0] == 1 and n_3[0] == 1) or \
        (n_1[1] == 1 and n_2[1] == 1 and n_3[1] == 1) or \
        (n_1[2] == 1 and n_2[2] == 1 and n_3[2] == 1) or \
        (n_1[0] == 1 and n_2[1] == 1 and n_3[2] == 1) or \
        (n_1[2] == 1 and n_2[1] == 1 and n_3[0] == 1) or \
        (n_1[0] == 1 and n_1[1] == 1 and n_1[2] == 1) or \
        (n_2[0] == 1 and n_2[1] == 1 and n_2[2] == 1) or \
            (n_3[0] == 1 and n_3[1] == 1 and n_3[2] == 1):
        first_win = True

    elif (n_1[0] == 2 and n_2[0] == 2 and n_3[0] == 2) or \
        (n_1[1] == 2 and n_2[1] == 2 and n_3[1] == 2) or \
        (n_1[2] == 2 and n_2[2] == 2 and n_3[2] == 2) or \
        (n_1[0] == 2 and n_2[1] == 2 and n_3[2] == 2) or \
        (n_1[2] == 2 and n_2[1] == 2 and n_3[0] == 2) or \
        (n_1[0] == 2 and n_1[1] == 2 and n_1[2] == 2) or \
        (n_2[0] == 2 and n_2[1] == 2 and n_2[2] == 2) or \
            (n_3[0] == 2 and n_3[1] == 2 and n_3[2] == 2):
        second_win = True

    else:
        draw = True

    return first_win, second_win, draw


action = game()

if first_win:
    print("First player won")
elif second_win:
    print("Second player won")
elif draw:
    print("Draw!")