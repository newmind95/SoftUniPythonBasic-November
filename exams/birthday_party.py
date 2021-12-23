number_of_bitcoins = int(input())
yuan = float(input())
comission = float(input())

one_bitcoin = 1168
leva = (number_of_bitcoins * one_bitcoin) + (yuan * 0.15 * 1.76)
price_in_euro = leva / 1.95
total_comission = price_in_euro * (comission / 100)
result = price_in_euro - total_comission

print('%.2f' % result)
