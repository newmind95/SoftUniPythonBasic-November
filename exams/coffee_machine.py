drink = input()
sugar = input()
number_of_drinks = int(input())

drink_price = 0
total_drink_price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        drink_price = 0.90
        total_drink_price = drink_price * number_of_drinks
        total_drink_price -= (total_drink_price * (35 / 100))
    elif sugar == 'Normal':
        drink_price = 1
        total_drink_price = drink_price * number_of_drinks
    elif sugar == 'Extra':
        drink_price = 1.20
        total_drink_price = drink_price * number_of_drinks

    if number_of_drinks >= 5:
        total_drink_price -= (total_drink_price * (25 / 100))

elif drink == 'Cappuccino':
    if sugar == 'Without':
        drink_price = 1.00
        total_drink_price = drink_price * number_of_drinks
    elif sugar == 'Normal':
        drink_price = 1.20
        total_drink_price = drink_price * number_of_drinks
    elif sugar == 'Extra':
        drink_price = 1.60
        total_drink_price = drink_price * number_of_drinks

elif drink == 'Tea':
    if sugar == 'Without':
        drink_price = 0.50
        total_drink_price = drink_price * number_of_drinks
    elif sugar == 'Normal':
        drink_price = 0.60
        total_drink_price = drink_price * number_of_drinks
    elif sugar == 'Extra':
        drink_price = 0.70
        total_drink_price = drink_price * number_of_drinks

if total_drink_price >= 15:
    total_drink_price -= (total_drink_price * (20 / 100))

print(f'You bought {number_of_drinks} cups of {drink} for {total_drink_price:.2f} lv.')
