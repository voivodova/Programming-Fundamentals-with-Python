sequence = input().split()
board = sequence.copy()
moves = 0

while True:
    command = input()
    if command == "end":
        break

    index_1, index_2 = map(int, command.split())

    if index_1 == index_2 or index_1 < 0 or index_1 >= len(sequence) or index_2 < 0 or index_2 >= len(sequence):
        moves += 1
        middle_index = len(sequence) // 2
        element = f"-{moves}a"
        sequence.insert(middle_index, element)
        sequence.insert(middle_index, element)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[index_1] == sequence[index_2]:
            element = sequence[index_1]
            sequence.remove(element)
            sequence.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break

if len(sequence) > 0:
    print("Sorry you lose :(")
    print(" ".join(board))
