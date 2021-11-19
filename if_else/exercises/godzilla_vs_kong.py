budged_for_film = float(input())
number_of_extras = int(input())
price_clothes_extras = float(input())

decor = 0.10
discount = 0.10

price_decor = (budged_for_film * decor)
price_clothes = number_of_extras * price_clothes_extras

if number_of_extras >= 150:
    price_clothes = price_clothes - (price_clothes * discount)

total_price = price_decor + price_clothes

if total_price > budged_for_film:
    print('Not enough money!')
    print(f'Wingard needs {total_price - budged_for_film:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budged_for_film - total_price:.2f} leva left.')
