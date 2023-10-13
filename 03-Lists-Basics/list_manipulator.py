initial_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    command_parts = command.split()
    cmd = command_parts[0]

    if cmd == "exchange":
        index = int(command_parts[1])
        if index < 0 or index >= len(initial_list):
            print("Invalid index")
            continue
        initial_list = initial_list[index + 1:] + initial_list[:index + 1]
    elif cmd == "max":
        parity = command_parts[1]
        if parity == "even":
            max_index = -1
            max_value = float("-inf")
            for i in range(len(initial_list)):
                if initial_list[i] % 2 == 0 and initial_list[i] >= max_value:
                    max_index = i
                    max_value = initial_list[i]
        else:
            max_index = -1
            max_value = float("-inf")
            for i in range(len(initial_list)):
                if initial_list[i] % 2 != 0 and initial_list[i] >= max_value:
                    max_index = i
                    max_value = initial_list[i]
        if max_index == -1:
            print("No matches")
        else:
            print(max_index)
    elif cmd == "min":
        parity = command_parts[1]
        if parity == "even":
            min_index = -1
            min_value = float("inf")
            for i in range(len(initial_list)):
                if initial_list[i] % 2 == 0 and initial_list[i] <= min_value:
                    min_index = i
                    min_value = initial_list[i]
        else:
            min_index = -1
            min_value = float("inf")
            for i in range(len(initial_list)):
                if initial_list[i] % 2 != 0 and initial_list[i] <= min_value:
                    min_index = i
                    min_value = initial_list[i]
        if min_index == -1:
            print("No matches")
        else:
            print(min_index)
    elif cmd == "first":
        count = int(command_parts[1])
        parity = command_parts[2]
        if count > len(initial_list):
            print("Invalid count")
            continue
        if parity == "even":
            result = [num for num in initial_list if num % 2 == 0][:count]
        else:
            result = [num for num in initial_list if num % 2 != 0][:count]
        print(result)
    elif cmd == "last":
        count = int(command_parts[1])
        parity = command_parts[2]
        if count > len(initial_list):
            print("Invalid count")
            continue
        if parity == "even":
            result = [num for num in initial_list if num % 2 == 0][-count:]
        else:
            result = [num for num in initial_list if num % 2 != 0][-count:]
        print(result)

print(initial_list)
