cars = int(input())

car_fuel = {}
car_mileage = {}

for _ in range(cars):
    car_args = input().split("|")
    car = car_args[0]
    mileage = int(car_args[1])
    fuel = int(car_args[2])

    car_fuel[car] = fuel
    car_mileage[car] = mileage

while True:
    line = input()
    if line == "Stop":
        break

    command_args = line.split(" : ")
    command = command_args[0]
    car = command_args[1]

    if command == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])

        if fuel > car_fuel[car]:
            print("Not enough fuel to make that ride")
            continue

        car_fuel[car] -= fuel
        car_mileage[car] += distance

        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if car_mileage[car] >= 100000:
            car_fuel.pop(car)
            car_mileage.pop(car)
            print(f"Time to sell the {car}!")

    elif command == "Refuel":
        fuel = int(command_args[2])
        before_refuel = car_fuel[car]
        car_fuel[car] = min(car_fuel[car] + fuel, 75)
        print(f"{car} refueled with {car_fuel[car] - before_refuel} liters")

    elif command == "Revert":
        kilometers = int(command_args[2])
        updated_mileage = car_mileage[car] - kilometers

        if updated_mileage < 10000:
            car_mileage[car] = 10000

        else:
            car_mileage[car] = updated_mileage
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in car_fuel.keys():
    fuel = car_fuel[car]
    mileage = car_mileage[car]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")