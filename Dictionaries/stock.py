initial_list = input().split()
food_type = {initial_list[i]: int(initial_list[i + 1]) for i in range(0, len(initial_list), 2)}

searching_for_food = input().split()
for product in searching_for_food:
    if product in food_type:
        print(f'We have {food_type[product]} of {product} left')
        continue

    print(f"Sorry, we don't have {product}")


