sequence = [int(element) for element in input().split()]
points = 0

while len(sequence) != 0:
    index = int(input())
    number = 0
    if 0 <= index < len(sequence):
        number = sequence.pop(index)
    elif 0 > index:
        num_to_add = sequence[-1]
        number = sequence[0]
        sequence[0] = sequence[-1]
    else:
        number_to_add = sequence[0]
        number = sequence[-1]
        sequence[-1] = sequence[0]
    points += number
    for current_index, current_number in enumerate(sequence):
        if current_number <= number:
            sequence[current_index] += number
        else:
            sequence[current_index] -= number

print(points)
