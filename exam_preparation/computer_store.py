prices = []
while True:
    price = input()
    if price == "special" or price == "regular":
        break
    price = float(price)
    if price <= 0:
        print("Invalid price!")
        continue
    prices.append(price)

if len(prices) == 0:
    print("Invalid order!")
else:
    total_price_without_taxes = sum(prices)
    taxes = total_price_without_taxes * 0.2
    total_price_with_taxes = total_price_without_taxes + taxes

    if price == "special":
        total_price_with_taxes *= 0.9

    print("Congratulations you've just bought a new computer!")
    print("Price without taxes: {:.2f}$".format(total_price_without_taxes))
    print("Taxes: {:.2f}$".format(taxes))
    print("-----------")
    print("Total price: {:.2f}$".format(total_price_with_taxes))
