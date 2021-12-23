import math

change = float(input())
coins = 0
change_to_cents = change * 100

while change_to_cents > 0:

    if change_to_cents >= 200:
        change_to_cents -= 200
        coins += 1
    elif change_to_cents >= 100:
        change_to_cents -= 100
        coins += 1
    elif change_to_cents >= 50:
        change_to_cents -= 50
        coins += 1
    elif change_to_cents >= 20:
        change_to_cents -= 20
        coins += 1
    elif change_to_cents >= 10:
        change_to_cents -= 10
        coins += 1
    elif change_to_cents >= 5:
        change_to_cents -= 5
        coins += 1
    elif change_to_cents >= 2:
        change_to_cents -= 2
        coins += 1
    elif change_to_cents >= 1:
        change_to_cents -= 1
        coins += 1

    change_to_cents = math.floor(change_to_cents)

print(coins)
