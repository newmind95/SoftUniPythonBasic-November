price_of_bag_over_20_kg = float(input())
bag_kg = float(input())
days_to_travelling = int(input())
number_of_bags = int(input())

price_of_bag = 0

if bag_kg < 10:
    price_of_bag = price_of_bag_over_20_kg * (20 / 100)
elif bag_kg <= 20:
    price_of_bag = price_of_bag_over_20_kg * (50 / 100)
else:
    price_of_bag = price_of_bag_over_20_kg

if days_to_travelling > 30:
    price_of_bag = price_of_bag + (price_of_bag * (10 / 100))
elif 7 <= days_to_travelling <= 30:
    price_of_bag = price_of_bag + (price_of_bag * (15 / 100))
elif days_to_travelling < 7:
    price_of_bag = price_of_bag + (price_of_bag * (40 / 100))

total_price = price_of_bag * number_of_bags

print(f"The total price of bags is: {total_price:.2f} lv.")
