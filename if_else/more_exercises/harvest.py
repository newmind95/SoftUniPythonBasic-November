vineyard = int(input())
grapes_one_square_root = float(input())
wine_liters_need = int(input())
number_employees = int(input())

discount = 0.40

total_grape = vineyard * grapes_one_square_root
total_wine = discount * total_grape / 2.5

difference = abs(wine_liters_need - total_wine)

if total_wine > wine_liters_need:
    print("Good harvest this year! Total wine:",
          round(total_wine), "liters.")
    print(round(difference), "liters left ->",
          round((difference / number_employees)), "liters per person.")
else:
    print("It will be a tough winter! More",round(difference), "liters wine needed.")
