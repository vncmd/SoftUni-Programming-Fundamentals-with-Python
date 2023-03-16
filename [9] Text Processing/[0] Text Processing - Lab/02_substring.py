first = input()
second = input()

while True:
    if first in second:
        second = second.replace(first, "")
    else:
        break

print(second)