def round_numbers(numbers):
    rounded_numbers = [round(num) for num in numbers]
    return rounded_numbers


input_numbers = input().split()
input_numbers = [float(num) for num in input_numbers]
rounded_list = round_numbers(input_numbers)
print(rounded_list)
