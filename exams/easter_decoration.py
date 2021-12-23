clients = int(input())
basket = 1.50
wreath = 3.80
chocolate_bunny = 7
counter = 0
total_price = 0
total_amount = 0

for client in range(clients):
    command = input()

    while command != 'Finish':

        if command == 'basket':
            counter += 1
            total_price += basket
        elif command == 'wreath':
            counter += 1
            total_price += wreath
        elif command == 'chocolate bunny':
            counter += 1
            total_price += chocolate_bunny
        command = input()

    if counter % 2 == 0:
        total_price *= 0.80

    if command == 'Finish':
        print(f'You purchased {counter} items for {total_price:.2f} leva.')

    total_amount += total_price
    counter = 0
    total_price = 0

average = total_amount / clients
print(f'Average bill per client is: {average:.2f} leva.')
