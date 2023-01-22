num = int(input())
start = 97

for first in range(start, start + num):
    for second in range(start, start + num):
        for third in range(start, start + num):
            result = f"{chr(first)}{chr(second)}{chr(third)}"
            print(result)
