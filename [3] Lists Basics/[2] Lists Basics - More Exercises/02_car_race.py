nums = input().split()

left_car = []
right_car = []

right_car_time = 0
middle = 0
left_car_time = 0

for idx in range(len(nums)):
    half = int(len(nums) / 2)
    left_car = nums[0:half]
    right_car = nums[half::]
    right_car.reverse()
    middle = int(right_car[-1])
    right_car.pop(-1)
    break

for idx in range(len(left_car)):
    current_index = int(left_car[idx])
    if current_index > 0:
        left_car_time += int(left_car[idx])
    elif current_index == 0:
        left_car_time = left_car_time * 0.80

for idx in range(len(right_car)):
    current_index = int(right_car[idx])
    if current_index > 0:
        right_car_time += int(right_car[idx])
    elif current_index == 0:
        right_car_time = right_car_time * 0.80

left_car_total = abs(left_car_time - middle)
right_car_total = abs(right_car_time - middle)

if left_car_total < right_car_total:
    print(f"The winner is left with total time: {left_car_time:.1f}")
elif right_car_total < left_car_total:
    print(f"The winner is right with total time: {right_car_time:.1f}")