budget = float(input())
season = input()
camp_price = 0
hotel_price = 0


if budget <= 100:
    if season == "summer":
        budget = budget * (30 / 100)
        camp_price = budget
        print("Somewhere in Bulgaria")
        print(f"Camp - {camp_price:.2f}")
    elif season == "winter":
        budget = budget * (70 / 100)
        hotel_price = budget
        print("Somewhere in Bulgaria")
        print(f"Hotel - {hotel_price:.2f}")
elif budget <= 1000:
    if season == "summer":
        budget = budget * (40 / 100)
        camp_price = budget
        print("Somewhere in Balkans")
        print(f"Camp - {camp_price:.2f}")
    elif season == "winter":
        budget = budget * (80 / 100)
        hotel_price = budget
        print("Somewhere in Balkans")
        print(f"Hotel - {hotel_price:.2f}")
else:
    budget = budget * (90 / 100)
    hotel_price = budget
    print("Somewhere in Europe")
    print(f"Hotel - {hotel_price:.2f}")

