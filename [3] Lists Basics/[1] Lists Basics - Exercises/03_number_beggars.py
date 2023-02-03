numbers = input().split(", ")
n_beggars = int(input())

beggars = [0] * n_beggars

for i in range(len(numbers)):
    beggars_i = i % n_beggars
    num = int(numbers[i])
    beggars[beggars_i] += num

print(beggars)
