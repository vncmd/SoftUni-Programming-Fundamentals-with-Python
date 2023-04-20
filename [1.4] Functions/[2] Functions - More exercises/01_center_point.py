from math import floor


def check_center_point(x, y):
    if x <= y:
        return f"({x1}, {x2})"
    elif y <= x:
        return f"({y_1}, {y_2})"


x1 = floor(float(input()))
x2 = floor(float(input()))

y_1 = floor(float(input()))
y_2 = floor(float(input()))

sum_axis_x = floor(abs(x1) + abs(x2))
sum_axis_y = floor(abs(y_1) + abs(y_2))

print(check_center_point(sum_axis_x, sum_axis_y))