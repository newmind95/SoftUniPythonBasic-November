number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
is_holiday = input()

price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
price = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2.00
    price_roses = 4.10
    price_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15

price = (number_of_chrysanthemums * price_chrysanthemums +
         number_of_roses * price_roses +
         number_of_tulips * price_tulips)

if is_holiday == "Y":
    price += price * (15 / 100)

if number_of_tulips > 7 and season == "Spring":
    price = price - (price * (5 / 100))
elif number_of_roses >= 10 and season == "Winter":
    price = price - (price * (10 / 100))

if (number_of_roses + number_of_tulips + number_of_chrysanthemums) >= 20:
    price = price - (price * (20 / 100))


total_price = price + 2

print(f"{total_price:.2f}")
