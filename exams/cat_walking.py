minute_for_walking_per_day = int(input())
number_of_walks_daily = int(input())
consumed_calories_per_day = int(input())

total_walking = minute_for_walking_per_day * number_of_walks_daily
total_burned_calories = total_walking * 5
consumed_calories = consumed_calories_per_day * (50 / 100)

if total_burned_calories > consumed_calories:
    print('Yes, the walk for your cat is enough.'
          ' Burned calories per day: %d.' % total_burned_calories)
else:
    print('No, the walk for your cat is not enough.'
          ' Burned calories per day: %d.' % total_burned_calories)
