destination = input()
date_reservation = input()
number_of_nights = int(input())
result = ""

if destination == "France":
    
    if date_reservation == "21-23":
        price_per_night = 30
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)
    elif date_reservation == "24-27":
        price_per_night = 35
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)
    elif date_reservation == "28-31":
        price_per_night = 40
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)

elif destination == "Italy":
    
    if date_reservation == "21-23":
        price_per_night = 28
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)
    elif date_reservation == "24-27":
        price_per_night = 32
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)
    elif date_reservation == "28-31":
        price_per_night = 39
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)

elif destination == "Germany":
    
    if date_reservation == "21-23":
        price_per_night = 32
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)
    elif date_reservation == "24-27":
        price_per_night = 37
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)
    elif date_reservation == "28-31":
        price_per_night = 43
        total_price = number_of_nights * price_per_night
        result = 'Easter trip to %s : %.2f leva.' % (destination, total_price)

print(result)
