n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])

        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]

    elif action == "Refuel":
        fuel = int(command[2])
        if cars[car]["fuel"] + fuel > 75:
            fuel = 75 - cars[car]["fuel"]
        cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(command[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
