sorting_complete = False

while not sorting_complete:
    name = input()

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")

    if name == "Welcome!":
        sorting_complete = True
print("Welcome to Hogwarts.")