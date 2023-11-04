number_cars = int(input())

class ParkingLot:
    def __init__(self):
        self.parking = {}

    def register(self, name, number):
        if name in self.parking:
            return f"ERROR: already registered with plate number {self.parking[name]}"

        self.parking[name] = number
        return f"{name} registered {number} successfully"

    def unregister(self, name):
        if name not in self.parking:
            return f"ERROR: user {name} not found"

        del self.parking[name]
        return f"{name} unregistered successfully"

    def __str__(self):
        return '\n'.join(f"{key} => {value}" for key, value in self.parking.items())

parking = ParkingLot()

for _ in range(number_cars):
    command, *data = input().split()
    print(parking.__getattribute__(command)(*data))

print(parking)
