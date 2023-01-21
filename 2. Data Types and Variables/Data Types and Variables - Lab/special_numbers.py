number = int(input())

for num in range(1, number + 1):
    flag = False
    num_as_str = str(num)
    total_sum = 0
    for char in num_as_str:
        total_sum += int(char)
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        flag = True
    print(f"{num} -> {flag}")



