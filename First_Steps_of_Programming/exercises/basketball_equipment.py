year_price_training = int(input())

price_basketball_shoes = year_price_training - year_price_training * 40 / 100
price_basketball_outfit = price_basketball_shoes - price_basketball_shoes * 20 / 100
price_basketball_ball = 1 / 4 * price_basketball_outfit
price_basketball_accessories = 1 / 5 * price_basketball_ball

price_outfit = year_price_training + \
               price_basketball_shoes + \
               price_basketball_outfit + \
               price_basketball_ball + \
               price_basketball_accessories

print(price_outfit)
