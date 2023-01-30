cards = input().split()
shuffle = int(input())
length = len(cards)
mid = int(length / 2)

for n_shuffles in range(shuffle):
    result_after_shuffle = []