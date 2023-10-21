quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
weight_in_kilograms = float(input())
quantity_food_in_grams = quantity_food_in_kilograms * 1000
quantity_hay_in_grams = quantity_hay_in_kilograms * 1000
quantity_cover_in_grams = quantity_cover_in_kilograms * 1000
weight_in_grams = weight_in_kilograms * 1000
is_food_not_left = False
month_days = 30

for day in range(1, month_days + 1):
    quantity_food_in_grams -= 300
    if quantity_food_in_grams <= 0:
        is_food_not_left = True

    if day % 2 == 0:
        quantity_hay_in_grams -= quantity_food_in_grams * (5 / 100)
        if quantity_hay_in_grams <= 0:
            is_food_not_left = True

    if day % 3 == 0:
        quantity_cover_in_grams -= weight_in_grams * 1 / 3
        if quantity_cover_in_grams <= 0:
            is_food_not_left = True

    if is_food_not_left:
        print('Merry must go to the pet store!')
        break

if not is_food_not_left:
    print('Everything is fine! Puppy is happy! ' \
          f'Food: {quantity_food_in_grams/1000:.2f}, ' \
          f'Hay: {quantity_hay_in_grams/1000:.2f}, ' \
      f'Cover: {quantity_cover_in_grams/1000:.2f}.')
