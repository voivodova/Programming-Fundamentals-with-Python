targets = list(map(int, input().split()))

def shoot_target(index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)

def add_target(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")

def strike_target(index, radius):
    start_index = index - radius
    end_index = index + radius
    if start_index >= 0 and end_index < len(targets):
        del targets[start_index:end_index+1]
    else:
        print("Strike missed!")

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    action = command[0]
    index = int(command[1])
    if action == "Shoot":
        power = int(command[2])
        shoot_target(index, power)
    elif action == "Add":
        value = int(command[2])
        add_target(index, value)
    elif action == "Strike":
        radius = int(command[2])
        strike_target(index, radius)

print("|".join(map(str, targets)))
