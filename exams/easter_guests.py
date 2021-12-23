from math import ceil

number_of_guests = int(input())
budget = int(input())

price_for_one_easter = 4
price_for_one_egg = 0.45

number_of_easter_need = ceil(number_of_guests / 3)
number_of_eggs_need = number_of_guests * 2

price_for_easter = price_for_one_easter * number_of_easter_need
price_for_eggs =  number_of_eggs_need * price_for_one_egg
total_price = price_for_easter + price_for_eggs

difference = abs(budget-total_price)

if budget > total_price:
    print('Lyubo bought %d Easter bread and %d eggs.' \
          % (number_of_easter_need, number_of_eggs_need))
    print('He has %.2f lv. left.' % difference)
else:
    print("Lyubo doesn't have enough money.")
    print('He needs %.2f lv. more.' % difference)
