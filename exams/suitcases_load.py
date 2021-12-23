trunk_capacity = float(input())
 
command = input()
counter_trunk_capacity = 0
is_capacity_end = False
 
while True:
 
    if command == 'End':
        print('Congratulations! All suitcases are loaded!')
        break
        
    suitcase_volume = float(command)
 
    if counter_trunk_capacity % 3 == 0:
        suitcase_volume += suitcase_volume * (10 / 100)
 
    if suitcase_volume > trunk_capacity:
        print('No more space!')
        is_capacity_end = True
        break
    
    trunk_capacity -= suitcase_volume
    counter_trunk_capacity += 1
    command = input()
 
print(f'Statistic: {counter_trunk_capacity} suitcases loaded.')
