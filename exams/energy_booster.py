fruit = input()
set_size = input()
number_of_purchased_sets = int(input())
energy_booster_price = 0
discount = 0

if set_size == 'small':
    if fruit == 'Watermelon':
        energy_booster_price += 2 * 56
    elif fruit == 'Mango':
        energy_booster_price += 2 * 36.66
    elif fruit == 'Pineapple':
        energy_booster_price += 2 * 42.10
    elif fruit == 'Raspberry':
        energy_booster_price += 2 * 20
elif set_size == 'big':
    if fruit == 'Watermelon':
        energy_booster_price += 5 * 28.70
    elif fruit == 'Mango':
        energy_booster_price += 5 * 19.60
    elif fruit == 'Pineapple':
        energy_booster_price += 5 * 24.80
    elif fruit == 'Raspberry':
        energy_booster_price += 5 * 15.20

price_set = number_of_purchased_sets * energy_booster_price

if 400 <= price_set <= 1000:
    discount = price_set * (15 / 100)
elif price_set > 1000:
    discount = price_set * (50 / 100)

total_price = abs(price_set - discount)
print('%.2f lv.' % total_price)
