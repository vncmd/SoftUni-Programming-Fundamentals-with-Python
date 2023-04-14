data = input()

nums, letters, output = [], [], []
[nums.append(int(x)) if x.isdigit() else letters.append(x) for x in data]

for itr in range(0, len(nums), 2):
    take, skip = nums[itr], nums[itr + 1]

    output += letters[:take]
    letters = letters[take + skip:]

print(*output, sep="")