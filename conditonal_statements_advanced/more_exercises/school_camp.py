season = input()        # Winter, Summer, Spring
type_of_group = input()     # boys, girls, mixed
number_of_students = int(input())       # integer between 1 and 10000
number_of_nights = int(input())         # integer between 1 and 100

price_for_one_night = 0
result = ''

if season == "Winter":
    if type_of_group == "girls" or type_of_group == "boys":
        price_for_one_night = 9.60
    elif type_of_group == "mixed":
        price_for_one_night = 10
elif season == "Spring":
    if type_of_group == "girls" or type_of_group == "boys":
        price_for_one_night = 7.20
    elif type_of_group == "mixed":
        price_for_one_night = 9.50
elif season == "Summer":
    if type_of_group == "girls" or type_of_group == "boys":
        price_for_one_night = 15
    elif type_of_group == "mixed":
        price_for_one_night = 20

total_price = number_of_students * price_for_one_night * number_of_nights

if number_of_students >= 50:
    total_price = total_price - (total_price * (50 / 100))
elif 20 <= number_of_students < 50:
    total_price = total_price - (total_price * (15 / 100))
elif 10 <= number_of_students < 20:
    total_price = total_price - (total_price * (5 / 100))

if season == "Winter":
    if type_of_group == "girls":
        result = f"Gymnastics {total_price:.2f} lv."
    elif type_of_group == "boys":
        result = f"Judo {total_price:.2f} lv."
    elif type_of_group == "mixed":
        result = f"Ski {total_price:.2f} lv."
elif season == "Spring":
    if type_of_group == "girls":
        result = f"Athletics {total_price:.2f} lv."
    elif type_of_group == "boys":
        result = f"Tennis {total_price:.2f} lv."
    elif type_of_group == "mixed":
        result = f"Cycling {total_price:.2f} lv."
elif season == "Summer":
    if type_of_group == "girls":
        result = f"Volleyball {total_price:.2f} lv."
    elif type_of_group == "boys":
        result = f"Football {total_price:.2f} lv."
    elif type_of_group == "mixed":
        result = f"Swimming {total_price:.2f} lv."

print(result)