def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lab_lst) or col >= len(lab_lst[0]):
        return True


def check_wall(row, col):
    if lab_lst[row][col] in "#v":
        return True


def exit_path(row, col):
    if row == 0 or row == len(lab_lst) - 1 or col == 0 or col == len(lab_lst[0]):
        return True


def starting_point():
    for pos_row, row in enumerate(lab_lst):
        for pos_col, col in enumerate(row):
            if col == "k":
                return pos_row, pos_col


def way_out_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col):
        return

    steps.append(1)

    if exit_path(row, col):
        max_length.append(sum(steps))

    lab[row][col] = "v"
    way_out_path(row, col + 1, lab)  # check right
    way_out_path(row, col - 1, lab)  # check left
    way_out_path(row + 1, col, lab)  # check up
    way_out_path(row - 1, col, lab)  # check down
    lab[row][col] = " "

    steps.pop()


maze = int(input())

lab_lst = []
steps = []
max_length = []

for curr_lab in range(maze):
    lab_lst.append(list(input()))

cols = len(lab_lst[0])
start_row, start_col = starting_point()

way_out_path(start_row, start_col, lab_lst)

if max_length:
    print(f"Kate got out in {max(max_length)} moves")
else:
    print("Kate cannot get out")
