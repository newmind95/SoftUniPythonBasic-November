type_of_league = input()
ticket_type = input()
number_of_tickets = int(input())
photo_with_trophy = input()

ticket_price = 0

if type_of_league == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50

    elif ticket_type == 'Premium':
        ticket_price = 105.20

    elif ticket_type == 'VIP':
        ticket_price = 118.90

elif type_of_league == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88

    elif ticket_type == 'Premium':
        ticket_price = 125.22

    elif ticket_type == 'VIP':
        ticket_price = 300.40

elif type_of_league == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.10

    elif ticket_type == 'Premium':
        ticket_price = 160.66
        
    elif ticket_type == 'VIP':
        ticket_price = 400

total_price_for_ticket = number_of_tickets * ticket_price

if total_price_for_ticket > 4000:
    total_price_for_ticket = total_price_for_ticket - (total_price_for_ticket * (25 / 100))

elif total_price_for_ticket > 2500:
    total_price_for_ticket = total_price_for_ticket - (total_price_for_ticket * (10 / 100))

    if photo_with_trophy == 'Y':
        photo_with_trophy_price = number_of_tickets * 40
        total_price_for_ticket += photo_with_trophy_price

print(f'{total_price_for_ticket:.2f}')
