employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students_count = int(input())

students_per_hour = employee1 + employee2 + employee3
total_time = 0

while students_count > 0:
    total_time += 1
    if total_time % 4 == 0:
        total_time += 1
    students_count -= students_per_hour

print(f"Time needed: {total_time}h.")
