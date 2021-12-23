height_in_centimeters_to_jump = int(input())
started_height = height_in_centimeters_to_jump - 30
counter_jumps = 0
unsuccessful = 0
is_record_improved = False

while True:

    height_from_jump = int(input())

    counter_jumps += 1

    if height_from_jump > started_height:
        if started_height >= height_in_centimeters_to_jump:
            is_record_improved = True
            break
        started_height += 5
        unsuccessful = 0
    else:
        unsuccessful += 1

    if unsuccessful == 3:
        break

if is_record_improved:
    print(f'Tihomir succeeded, he jumped over {height_in_centimeters_to_jump}'
          f'cm after {counter_jumps} jumps.')
else:
    print(f'Tihomir failed at {started_height}cm after {counter_jumps} jumps.')
    
        
