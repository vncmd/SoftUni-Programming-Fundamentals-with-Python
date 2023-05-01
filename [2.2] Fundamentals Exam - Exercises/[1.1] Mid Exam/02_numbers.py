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


# Different solution:

# nums = [int(num) for num in input().split()]

# sorted_nums = list(sorted(nums, reverse=True))
# avg_num = sum(sorted_nums) / len(sorted_nums)
# greater_value = []
#
# for num in range(len(sorted_nums)):
#     current_num = int(sorted_nums[num])
#
#     if current_num > avg_num:
#         greater_value.append(current_num)
#
# for num in range(len(greater_value)):
#     if len(greater_value) > 5:
#         greater_value.pop(-1)
#
# if not greater_value:
#     print("No")
#
# else:
#     print(*greater_value)
