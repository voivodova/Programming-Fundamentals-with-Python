days = int(input())
number_players = int(input())
total_energy = float(input())
person_water = float(input())
person_food = float(input())
total_water = 0.0
total_water = float(days * number_players * person_water)
total_food = 0.0
total_food = float(days * number_players * person_food)
water_day = 0
food_day = 0
for day in range(days):
    wasted_energy = float(input())
    total_energy -= wasted_energy
    if total_energy <= 0.0:
        break
    water_day += 1
    if water_day >= 2:
        total_water -= total_water * 0.3
        total_energy += total_energy * 0.05
        water_day = 0
    food_day += 1
    if food_day >= 3:
        total_food -= (total_food / number_players)
        total_energy += total_energy * 0.1
        food_day = 0

if total_energy >= 1:
    print(f"You are ready for the quest. You will be left with - {total_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f}"
          f" food and {total_water:.2f} water.")
