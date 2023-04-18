from math import floor


def center_point(sum1, sum2, sum3, sum4):
    first_total = sum1 + sum2
    second_total = sum3 + sum4
    if first_total > second_total:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif first_total < second_total:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"


x1, x2, y1, y2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))
x3, x4, y3, y4 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))

x_sum = floor(abs(x1) + abs(x2))
y_sum = floor(abs(y1) + abs(y2))
x2_sum = floor(abs(x3) + abs(x4))
y2_sum = floor(abs(y3) + abs(y4))

print(center_point(x_sum, y_sum, x2_sum, y2_sum))