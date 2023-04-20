first_str, second_str = input().split()
total_sum = 0

if len(first_str) > len(second_str):
    for idx in range(len(second_str)):
        total_sum += ord(first_str[idx]) * ord(second_str[idx])
    for idx in range(len(second_str), len(first_str)):
        total_sum += ord(first_str[idx])
elif len(second_str) > len(first_str):
    for idx in range(len(first_str)):
        total_sum += ord(first_str[idx]) * ord(second_str[idx])
    for idx in range(len(first_str), len(second_str)):
        total_sum += ord(second_str[idx])
else:
    for idx in range(len(second_str)):
        total_sum += ord(first_str[idx]) * ord(second_str[idx])
print(total_sum)