people_waiting = int(input())
lift_state = [int(x) for x in input().split()]

for i in range(len(lift_state)):
    while lift_state[i] < 4 and people_waiting > 0:
        lift_state[i] += 1
        people_waiting -= 1

is_full = all(x == 4 for x in lift_state)
has_empty_spots = any(x < 4 for x in lift_state)

if is_full and people_waiting == 0:
    print(" ".join(str(x) for x in lift_state))
elif has_empty_spots and people_waiting == 0:
    print("The lift has empty spots!")
    print(" ".join(str(x) for x in lift_state))
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(str(x) for x in lift_state))
