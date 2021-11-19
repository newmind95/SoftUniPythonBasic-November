budget = float(input())
season = input()

if budget <= 100:
    print('Economy class')
    if season == "Summer":
        budget = budget * (35 / 100)
        print(f"Cabrio - {budget:.2f}")
    elif season == "Winter":
        budget = budget * (65 / 100)
        print(f"Jeep - {budget:.2f}")
elif 100 < budget <= 500:
    print('Compact class')
    if season == "Summer":
        budget = budget * (45 / 100)
        print(f"Cabrio - {budget:.2f}")
    elif season == "Winter":
        budget = budget * (80 / 100)
        print(f"Jeep - {budget:.2f}")
else:
    print('Luxury class')
    if season == "Summer" or season == "Winter":
        budget = budget * (90 / 100)
        print(f"Jeep - {budget:.2f}")
