int_lists = input().split()
nums_remove = int(input())

current_list = []
for num in range(len(int_lists)):
    current_list.append(int(int_lists[num]))

for index in range(nums_remove):
    current_list.remove(min(current_list))

print(*current_list, sep=', ')



