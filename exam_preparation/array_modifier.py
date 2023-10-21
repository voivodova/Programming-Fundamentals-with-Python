array = list(map(int, input().split()))

command = input()

while command != "end":
    command_args = command.split()
    action = command_args[0]

    if action == "swap":
        index1 = int(command_args[1])
        index2 = int(command_args[2])
        array[index1], array[index2] = array[index2], array[index1]

    elif action == "multiply":
        index1 = int(command_args[1])
        index2 = int(command_args[2])
        array[index1] *= array[index2]

    elif action == "decrease":
        array = [num - 1 for num in array]

    command = input()

print(", ".join(map(str, array)))
