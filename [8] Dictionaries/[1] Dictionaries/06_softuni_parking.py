parking = {}
number_of_cars = int(input())
for car in range(number_of_cars):
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