lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    command_parts = command.split(":")
    action = command_parts[0]
    lesson_title = command_parts[1]

    if action == "Add":
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    elif action == "Insert":
        index = int(command_parts[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in lessons:
            lessons.remove(lesson_title)
            if f"{lesson_title}-Exercise" in lessons:
                lessons.remove(f"{lesson_title}-Exercise")

    elif action == "Swap":
        lesson_title2 = command_parts[2]
        if lesson_title in lessons and lesson_title2 in lessons:
            index1 = lessons.index(lesson_title)
            index2 = lessons.index(lesson_title2)
            lessons[index1], lessons[index2] = lessons[index2], lessons[index1]

            if f"{lesson_title}-Exercise" in lessons:
                exercise_index = lessons.index(f"{lesson_title}-Exercise")
                lessons.remove(f"{lesson_title}-Exercise")
                lessons.insert(index2+1, f"{lesson_title}-Exercise")

            if f"{lesson_title2}-Exercise" in lessons:
                exercise_index2 = lessons.index(f"{lesson_title2}-Exercise")
                lessons.remove(f"{lesson_title2}-Exercise")
                lessons.insert(index1+1, f"{lesson_title2}-Exercise")

    elif action == "Exercise":
        if lesson_title in lessons:
            index = lessons.index(lesson_title)
            if f"{lesson_title}-Exercise" not in lessons:
                lessons.insert(index+1, f"{lesson_title}-Exercise")
        else:
            lessons.append(lesson_title)
            lessons.append(f"{lesson_title}-Exercise")

for i, lesson in enumerate(lessons):
    print(f"{i+1}.{lesson}")

