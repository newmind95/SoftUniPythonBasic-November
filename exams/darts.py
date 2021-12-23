name_of_player = input()

starting_points = 301
successed_shots = 0
unsuccessed_shots = 0
command = input()

while command != 'Retire':
    field = command
    points = int(input())
    
    if field == 'Single':
        points *= 1
        starting_points -= points
        if 0 <= starting_points:
            successed_shots += 1
        else:
            unsuccessed_shots += 1
            starting_points += points
        
    elif field == 'Double':
        points *= 2
        starting_points -= points
        if 0 <= starting_points:
            successed_shots += 1
        else:
            unsuccessed_shots += 1
            starting_points += points
            
    elif field == 'Triple':
        points *= 3
        starting_points -= points
        if 0 <= starting_points:
            successed_shots += 1
        else:
            unsuccessed_shots += 1
            starting_points += points

    if starting_points == 0:
        print(f'{name_of_player} won the leg with {successed_shots} shots.')
        break

    command = input()

    if command == 'Retire':
        print(f'{name_of_player} retired after {unsuccessed_shots} unsuccessful shots.')
