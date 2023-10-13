budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price

colored_eggs = 0
loaves = 0

while budget >= flour_price + eggs_price + milk_price / 4:
    budget -= flour_price + eggs_price + milk_price / 4
    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

money_left = "{:.2f}".format(budget)
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left.")