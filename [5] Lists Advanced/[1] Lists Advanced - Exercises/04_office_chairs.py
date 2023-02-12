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
