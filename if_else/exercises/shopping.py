budget = float(input())
number_video_cards = int(input())
number_processor = int(input())
number_ram = int(input())

video_card = 250
price_video_cards = number_video_cards * video_card

processor = price_video_cards * 0.35
price_processor = number_processor * processor

ram = price_video_cards * 0.10
price_ram = number_ram * ram

total_price = price_video_cards + price_ram + price_processor

if number_video_cards > number_processor:
    total_price = total_price - (total_price * 0.15)

if total_price < budget:
    print(f"You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")