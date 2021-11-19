number_of_kilometers = int(input())     # number of kilometers - integer between 1 and 5000
day_or_night_traveling = input()        # traveling in the day or in the night

ticket_price_for_one_km = 0
total_price = 0

if day_or_night_traveling == "day":
    ticket_price_for_one_km = 0.79
    total_price = 0.70 + number_of_kilometers * ticket_price_for_one_km
elif day_or_night_traveling == "night":
    ticket_price_for_one_km = 0.90
    total_price = 0.70 + number_of_kilometers * ticket_price_for_one_km

if number_of_kilometers >= 20:
    ticket_price_for_one_km = 0.09
    total_price = number_of_kilometers * ticket_price_for_one_km

if number_of_kilometers >= 100:
    ticket_price_for_one_km = 0.06
    total_price = number_of_kilometers * ticket_price_for_one_km

print(f"{total_price:.2f}")