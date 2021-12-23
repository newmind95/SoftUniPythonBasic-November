income = int(input())

command = input()
total_cocteils_price = 0

while command != 'Party!':
    
    name_of_cocteil = command
    price_of_cocteil = len(name_of_cocteil)
    
    number_of_cocteils = int(input())
    price_of_cocteil *= number_of_cocteils
    if price_of_cocteil % 2 != 0:
        price_of_cocteil -= (price_of_cocteil * (25 / 100))
    total_cocteils_price += price_of_cocteil

    if total_cocteils_price > income:
        print('Target acquired.')
        break

    command = input()
    if command == 'Party!':
        income -= total_cocteils_price
        print(f'We need {abs(income):.2f} leva more.')

print(f'Club income = {total_cocteils_price:.2f} leva.')
