price_travel = float(input())
number_puzzles = int(input())
number_talk_babies = int(input())
number_bear = int(input())
number_minions = int(input())
number_tir = int(input())

price_puzzle = 2.60
price_talk_baby = 3
price_bear = 4.10
price_minion = 8.20
price_tir = 2
pechalba = 0
naem = 0

discount = 0.25

sum_of_all_products = (number_puzzles * price_puzzle) + \
      (number_talk_babies * price_talk_baby) + \
      (number_bear * price_bear) + \
      (number_minions * price_minion) + \
      (number_tir * price_tir)

number_of_toys = number_puzzles + number_talk_babies + number_bear + \
        number_minions + number_tir

if number_of_toys >= 50:
    sum_of_all_products = sum_of_all_products - (sum_of_all_products * discount)

naem += sum_of_all_products * 0.10
pechalba += sum_of_all_products - naem

if pechalba >= price_travel:
    print(f"Yes! {pechalba - price_travel:.2f} lv left.")
else:
    print(f"Not enough money! {price_travel - pechalba:.2f} lv needed.")
