quantity_eggs = int(input())
is_quit = False
total_sold_eggs = 0
total_left_eggs = 0

while not is_quit:
    command = input()

    if command == 'Close':
        is_quit = True
        break

    number_of_eggs = int(input())
    
    if command == 'Buy':
        total_left_eggs += quantity_eggs
        if number_of_eggs <= total_left_eggs:
            total_left_eggs -= number_of_eggs
            total_sold_eggs += number_of_eggs
        else:
            print('Not enough eggs in store!')
            print(f'You can buy only {total_left_eggs}.')
            break

    elif command == 'Fill':
        total_left_eggs += number_of_eggs
            
if is_quit:
    print('Store is closed!')
    print(f'{total_sold_eggs} eggs sold.')
