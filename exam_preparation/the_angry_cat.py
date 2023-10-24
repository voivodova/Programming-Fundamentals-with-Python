items = input().split(", ")
entry_point = int(input())
item_type = input()

left_sum = 0
right_sum = 0

for i in range(entry_point - 1, -1, -1):
    if item_type == "cheap" and int(items[i]) < int(items[entry_point]):
        left_sum += int(items[i])
    elif item_type == "expensive" and int(items[i]) >= int(items[entry_point]):
        left_sum += int(items[i])

for i in range(entry_point + 1, len(items)):
    if item_type == "cheap" and int(items[i]) < int(items[entry_point]):
        right_sum += int(items[i])
    elif item_type == "expensive" and int(items[i]) >= int(items[entry_point]):
        right_sum += int(items[i])

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
