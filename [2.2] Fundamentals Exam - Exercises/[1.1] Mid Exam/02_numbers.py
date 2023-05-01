main_list = [int(x) for x in input().split()]

avg_num = sum(main_list) / len(main_list)

main_list.sort(reverse=True)
print_numbers = False

for idx, num in enumerate(main_list):
    if idx <= 4 and num > avg_num:
        print(num, end=" ")

        print_numbers = True

    if not print_numbers:
        print("No")

        break
