food_kgs = float(input()) * 1000
hay_kgs = float(input()) * 1000
cover_kgs = float(input()) * 1000
weight_kgs = float(input()) * 1000

cover = weight_kgs / 3
food_eaten = 0

for day in range(1, 31):
    food_eaten += 300
    food_kgs -= 300
    if day % 2 == 0:
        hay = food_kgs * 0.05
        hay_kgs -= hay
        food_eaten += hay

    if day % 3 == 0:
        cover_kgs -= cover

if food_kgs > 0 and hay_kgs > 0 and cover_kgs > 0:

    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food_kgs/1000:.2f}, "
          f"Hay: {hay_kgs/1000:.2f}, "
          f"Cover: {cover_kgs/1000:.2f}."
          )

else:
    print("Merry must go to the pet store!")
