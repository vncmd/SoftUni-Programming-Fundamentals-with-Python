parking = {}
drivers = int(input())
for car in range(drivers):
    current_driver = input().split()
    action = current_driver[0]
    if action == "register":
        username = current_driver[1]
        license_plate_number = current_driver[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        username = current_driver[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")

# Different solution:


# def register_car(name, number):
#     if name in parking_data:
#         print(f"ERROR: already registered with plate number {parking_data[name]}")
#         return
#     parking_data[name] = number
#     print(f"{name} registered {number} successfully")
#
#
# def unregister_car(name):
#     if name not in parking_data:
#         print(f"ERROR: user {name} not found")
#         return
#     del parking_data[name]
#     print(f"{name} unregistered successfully")
#
#
# def all_cars():
#     for key, value in parking_data.items():
#         print(f"{key} => {value}")
#
#
# number_cars = int(input())
# parking_data = {}
#
# for _ in range(number_cars):
#     command, name, *number = input().split()
#     if command == "register":
#         number = number[-1]
#         register_car(name, number)
#     else:
#         unregister_car(name)
#
# all_cars()
