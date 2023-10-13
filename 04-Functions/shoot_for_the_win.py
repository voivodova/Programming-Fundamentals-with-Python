targets_sequence = list(map(int, input().split()))

shot_targets = 0

while True:
    command = input()
    if command == "End":
        break

    target_index = int(command)

    if target_index < 0 or target_index >= len(targets_sequence):
        continue

    if targets_sequence[target_index] == -1:
        continue

    shot_value = targets_sequence[target_index]
    targets_sequence[target_index] = -1
    shot_targets += 1

    for i in range(len(targets_sequence)):
        if targets_sequence[i] == -1:
            continue
        if targets_sequence[i] > shot_value:
            targets_sequence[i] -= shot_value
        else:
            targets_sequence[i] += shot_value

print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets_sequence))}")
