number_of_joinery = int(input())
type_of_joinery = input()
shipment_method = input()
price = 0

if number_of_joinery <= 10:
    print('Invalid order')
else:

    if type_of_joinery == "90X130":
        unit_price = 110
        price = number_of_joinery * unit_price
        if 30 < number_of_joinery <= 60:
            price = price - (price * (5 / 100))
        elif number_of_joinery > 60:
            price = price - (price * (8 / 100))

    elif type_of_joinery == "100X150":
        unit_price = 140
        price = number_of_joinery * unit_price
        if 40 < number_of_joinery <= 80:
            price = price - (price * (6 / 100))
        elif number_of_joinery > 80:
            price = price - (price * (10 / 100))

    elif type_of_joinery == "130X180":
        unit_price = 190
        price = number_of_joinery * unit_price
        if 20 < number_of_joinery <= 50:
            price = price - (price * (7 / 100))
        elif number_of_joinery > 50:
            price = price - (price * (12 / 100))

    elif type_of_joinery == "200X300":
        unit_price = 250
        price = number_of_joinery * unit_price
        if 25 < number_of_joinery <= 50:
            price = price - (price * (9 / 100))
        elif number_of_joinery > 50:
            price = price - (price * (14 / 100))

    if shipment_method == "With delivery":
        price = price + 60

    if number_of_joinery >= 100:
        price = price - (price * (4 / 100))

    print('%.2f BGN' % price)