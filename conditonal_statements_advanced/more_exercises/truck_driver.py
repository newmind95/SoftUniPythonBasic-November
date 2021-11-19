season = input()
kilometers_for_month = float(input())

price_for_one_kilometer = 0

if kilometers_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_for_one_kilometer = 0.75
    elif season == "Summer":
        price_for_one_kilometer = 0.90
    elif season == "Winter":
        price_for_one_kilometer = 1.05
elif 5000 < kilometers_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_for_one_kilometer = 0.95
    elif season == "Summer":
        price_for_one_kilometer = 1.10
    elif season == "Winter":
        price_for_one_kilometer = 1.25
elif 10000 < kilometers_for_month <= 20000:
    if season == "Spring" or season == "Autumn" \
            or season == "Summer" or season == "Winter":
        price_for_one_kilometer = 1.45

salary = kilometers_for_month * price_for_one_kilometer
salary *= 4
salary = salary - (salary * (10 / 100))
print(f"{salary:.2f}")