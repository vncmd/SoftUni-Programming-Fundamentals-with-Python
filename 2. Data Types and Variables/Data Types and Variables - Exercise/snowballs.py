num_snowball = int(input())

highest_snowball = 0
best_snowball = float("-inf")
for i in range(num_snowball):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality
    if value > best_snowball:
        best_snowball = value
        print(f"{weight} : {time} = {value} ({quality})")

