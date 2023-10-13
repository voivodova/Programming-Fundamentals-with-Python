def find_even_indices(numbers):
    number_list = numbers.split(", ")

    even_indices = []

    for i in range(len(number_list)):
        if int(number_list[i]) % 2 == 0:
            even_indices.append(i)

    print(even_indices)


input_string = input()

find_even_indices(input_string)
