numbers = input()
numbers_list = list(map(int, numbers.split()))

minimum_number = min(numbers_list)
maximum_number = max(numbers_list)
sum_of_number = sum(numbers_list)

print("The minimum number is", minimum_number)
print("The maximum number is", maximum_number)
print("The sum number is:", sum_of_number)
