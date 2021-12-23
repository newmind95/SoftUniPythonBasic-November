number_of_days = int(input())
total_food = float(input())

total_dog_food_eaten = 0
total_cat_food_eaten = 0
total_biscuits_eaten = 0
total_food_eaten = 0

for day in range(1, number_of_days + 1):

    dog_food_eaten = int(input())
    total_dog_food_eaten += dog_food_eaten

    cat_food_eaten = int(input())
    total_cat_food_eaten += cat_food_eaten
    total_food_eaten += dog_food_eaten + cat_food_eaten

    if day % 3 == 0:
        total_biscuits_eaten += (dog_food_eaten + cat_food_eaten) * 0.10

biscuits = round(total_biscuits_eaten)
percentage_total_food_eaten = (total_food_eaten / total_food) * 100
percentage_dog_food_eaten = (total_dog_food_eaten / total_food_eaten) * 100
percentage_cat_food_eaten = (total_cat_food_eaten / total_food_eaten) * 100
print(f'Total eaten biscuits: {biscuits}gr.')
print(f'{percentage_total_food_eaten}% of the food has been eaten.')
print(f'{percentage_dog_food_eaten}% eaten from the dog.')
print(f'{percentage_cat_food_eaten}% eaten from the cat.')
