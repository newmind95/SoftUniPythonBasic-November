from math import floor, ceil

number_of_days_she_travels = int(input())
food_left_in_kg = int(input())
food_for_dog_per_day_in_kg = float(input())
food_for_cat_per_day_in_kg = float(input())
food_for_turtle_per_day_in_g = float(input())

food_for_dog_need = number_of_days_she_travels * food_for_dog_per_day_in_kg
food_for_cat_need = number_of_days_she_travels * food_for_cat_per_day_in_kg
food_for_turtle_need = number_of_days_she_travels * food_for_turtle_per_day_in_g / 1000

total_food = food_for_dog_need + food_for_cat_need + food_for_turtle_need

difference = abs(total_food - food_left_in_kg)

if total_food < food_left_in_kg:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
