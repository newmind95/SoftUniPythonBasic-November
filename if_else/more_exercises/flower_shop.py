from math import floor, ceil

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
price_for_gift = float(input())

price_for_magnolias = 3.25
price_for_hyacinths = 4
price_for_roses = 3.50
price_for_cacti = 8

total_price = (number_of_magnolias * price_for_magnolias) \
    + (number_of_hyacinths * price_for_hyacinths) \
    + (number_of_roses * price_for_roses) \
    + (number_of_cacti * price_for_cacti)

profit = total_price - (total_price * (5 / 100))

difference = abs(profit - price_for_gift)

if profit < price_for_gift:
    print(f"She will have to borrow {ceil(difference)} leva.")
else:
    print(f"She is left with {floor(difference)} leva.")
