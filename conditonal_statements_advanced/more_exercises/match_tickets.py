budget = float(input())
category = input()
number_of_fans_in_group = int(input())

transport = 0
price_ticket = 0
vip = 499.99
normal = 249.99

if 1 <= number_of_fans_in_group <= 4:
    transport = budget * (75 / 100)
elif 5 <= number_of_fans_in_group <= 9:
    transport = budget * (60 / 100)
elif 10 <= number_of_fans_in_group <= 24:
    transport = budget * (50 / 100)
elif 25 <= number_of_fans_in_group <= 49:
    transport = budget * (40 / 100)
else:
    transport = budget * (25 / 100)

difference = abs(budget - transport)

if category == "Normal":
    price_ticket = number_of_fans_in_group * normal
elif category == "VIP":
    price_ticket = number_of_fans_in_group * vip

if price_ticket < difference:
    total_price_for_ticket = difference - price_ticket
    print(f"Yes! You have {total_price_for_ticket:.2f} leva left.")
else:
    total_price_for_ticket = price_ticket - difference
    print(f"Not enough money! You need {total_price_for_ticket:.2f} leva.")