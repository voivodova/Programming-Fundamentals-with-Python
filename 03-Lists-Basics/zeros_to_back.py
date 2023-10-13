def move_zeros_to_back(input_string):
    numbers = list(map(int, input_string.split(", ")))

    zeros_count = numbers.count(0)
    numbers = [num for num in numbers if num != 0]

    numbers += [0] * zeros_count


    print(numbers)


input_string = input()
move_zeros_to_back(input_string)
