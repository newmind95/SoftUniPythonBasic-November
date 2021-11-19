budget_for_fishing_group = int(input())
season = input()
number_of_fisherman = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if number_of_fisherman <= 6:
    boat_rent = boat_rent - (boat_rent * (10 / 100))
elif number_of_fisherman <= 11:
    boat_rent = boat_rent - (boat_rent * (15 / 100))
else:
    boat_rent = boat_rent - (boat_rent * (25 / 100))

if season != "Autumn" and number_of_fisherman % 2 == 0:
    boat_rent = boat_rent - (boat_rent * (5 / 100))

difference = abs(budget_for_fishing_group - boat_rent)

if budget_for_fishing_group >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")