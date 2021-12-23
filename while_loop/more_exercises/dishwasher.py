quantity_detergent = 750
dishes_count = 0
pots_count = 0
counter = 0
detergent_left = 0
is_machine_end = False
total_quantity_detergent = int(input())
total_quantity_detergent *= quantity_detergent

while total_quantity_detergent >= 0:
    command = input()
    if command == 'End':
        is_machine_end = True
        break

    dishes_to_wash = int(command)
    counter += 1

    if counter % 3 == 0:
        needed_detergent = dishes_to_wash * 15
        total_quantity_detergent -= needed_detergent

        if total_quantity_detergent >= 0:
            pots_count += dishes_to_wash

    else:
        needed_detergent = dishes_to_wash * 5
        total_quantity_detergent -= needed_detergent
        if total_quantity_detergent >= 0:
            dishes_count += dishes_to_wash
    

if is_machine_end:
    print('Detergent was enough!')
    print(f'{dishes_count} dishes and {pots_count} pots where washed.')
    print(f'Leftover detergent {total_quantity_detergent}')
else:
    print(f'Not enough detergent, {abs(total_quantity_detergent)} ml.more necessary!')
    
