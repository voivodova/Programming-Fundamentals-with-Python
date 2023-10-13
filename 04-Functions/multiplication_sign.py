num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
count = 0
zero = False
new_list = [num_1, num_2, num_3]
for i in range(len(new_list)):
    if num_3 == 0 or num_2 == 0 or num_1 == 0:
        zero = True
        break
    elif new_list[i] < 0:
        count += 1

if count == 1 or count == 3:
    print("negative")
elif zero:
    print("zero")
else:
    print("positive")
