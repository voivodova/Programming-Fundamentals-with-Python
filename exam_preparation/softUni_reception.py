employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())

sum_of_ee = employee1_efficiency + employee2_efficiency + employee3_efficiency
hours = students_count // sum_of_ee
if students_count % sum_of_ee != 0:
    hours += 1
for h in range(1, hours + 1):
    if h % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")
