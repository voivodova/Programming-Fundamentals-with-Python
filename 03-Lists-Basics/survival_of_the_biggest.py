numbers_str = input().split()
numbers = []

for number in numbers_str:
    numbers.append(int(number))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")
