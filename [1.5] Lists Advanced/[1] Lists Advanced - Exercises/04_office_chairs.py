rooms = int(input())

free_chairs = 0
flag = True
for n_room in range(1, rooms + 1):
    chairs, guests_str = input().split()
    guests = int(guests_str)

    if guests > len(chairs):
        n_chairs = guests - len(chairs)
        print(f"{n_chairs} more chairs needed in room {n_room}")
        flag = False
    else:
        free_chairs_row = len(chairs) - guests
        free_chairs += free_chairs_row

if flag:
    print(f"Game On, {free_chairs} free chairs left")

# Different solution:


# def rooms_check(numbers_of_rooms):
#     total_free_chairs = 0
#     total_needed_chairs = 0
#
#     for room in range(1, numbers_of_rooms + 1):
#         free_chairs, visitors = input().split()
#         diff = len(free_chairs) - int(visitors)
#
#         if diff >= 0:
#             total_free_chairs += diff
#         else:
#             total_needed_chairs += abs(diff)
#             print(f"{abs(diff)} more chairs needed in room {room}")
#
#     return total_free_chairs, total_needed_chairs
#
#
# number_of_rooms = int(input())
# free_chairs, needed_chairs = rooms_check(number_of_rooms)
#
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")
