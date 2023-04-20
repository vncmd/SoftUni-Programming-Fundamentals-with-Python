import math

n_people = int(input())
capacity = int(input())

courses = math.ceil(n_people / capacity)
print(courses)
