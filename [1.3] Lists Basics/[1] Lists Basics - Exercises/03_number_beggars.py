numbers = input().split(", ")
n_beggars = int(input())

beggars = [0] * n_beggars

for i in range(len(numbers)):
    beggars_idx = i % n_beggars
    num = int(numbers[i])
    beggars[beggars_idx] += num

print(beggars)

# Different solution:

# money = input().split(", ")
# money_num = []
#
# for el in money:
#     money_num.append(int(el))
#
# beggars = int(input())
# total_sum = []
# start_idx = 0
#
# while start_idx < beggars:
#     current_beggar_cut = 0
#     for current_idx in range(start_idx, len(money_num), beggars):
#         current_beggar_cut += money_num[current_idx]
#     total_sum.append(current_beggar_cut)
#     start_idx += 1
#
# print(total_sum)
