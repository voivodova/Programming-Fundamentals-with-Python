sequence = input()
numbers = sequence.split()

numbers = [int(num) for num in numbers]
sorted_numbers = sorted(numbers)

print(sorted_numbers)
