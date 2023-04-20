n = int(input())

highest_snowball = 0
best_snowball = float("-inf")
output = ""
for idx in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight // time) ** quality

    if result > best_snowball:
        best_snowball = result
        output = f"{weight} : {time} = {result} ({quality})"

print(output)

