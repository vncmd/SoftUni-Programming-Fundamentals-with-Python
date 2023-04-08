from math import floor


def check_center_point(x, y):
    if x <= y:
        return f"({first_point_x}, {second_point_x})"
    elif y <= x:
        return f"({first_point_y}, {second_point_y})"


first_point_x = floor(float(input()))
second_point_x = floor(float(input()))

first_point_y = floor(float(input()))
second_point_y = floor(float(input()))

sum_axis_x = floor(abs(first_point_x) + abs(second_point_x))
sum_axis_y = floor(abs(first_point_y) + abs(second_point_y))

print(check_center_point(sum_axis_x, sum_axis_y))