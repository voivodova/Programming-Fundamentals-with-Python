people = int(input())
lift_state = list(map(int, input().split()))

for i in range(len(lift_state)):
    while lift_state[i] < 4:
        if people == 0:
            break
        lift_state[i] += 1
        people -= 1

lift_full = all(x == 4 for x in lift_state)
lift_empty_spots = any(x < 4 for x in lift_state)

if lift_full and people == 0:
    print(" ".join(map(str, lift_state)))
elif lift_empty_spots and people == 0:
    print("The lift has empty spots!")
    print(" ".join(map(str, lift_state)))
elif not lift_full and people == 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(map(str, lift_state)))
