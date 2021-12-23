budget = float(input())
product_counter = 0
total_price = 0

while True:

    product_name = input()
    if product_name == 'Stop':
        print(f'You bought {product_counter} products for {total_price:.2f} leva.')
        break

    product_price = float(input())

    product_counter += 1

    if product_counter % 3 == 0:
        total_price += product_price / 2
    else:
        total_price += product_price

    if total_price > budget:
        difference = abs(total_price - budget)
        print("You don't have enough money!")
        print(f'You need {difference} leva!')
        break
