purchased_quality_dog_food = int(input())

command = input()
food_in_grams = purchased_quality_dog_food * 1000
total_food_eaten = 0

while True:

    if command == 'Adopted':
        break

    eated_food = int(command)
    total_food_eaten += eated_food
    
    command = input()

difference = abs(total_food_eaten - food_in_grams)

if total_food_eaten <= food_in_grams:
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    print(f'Food is not enough. You need {difference} grams more.')
