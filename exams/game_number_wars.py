name_of_first_player = input()
name_of_second_player = input()

first_player_points = 0
second_player_points = 0
command = input()

while command != 'End of game':

    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_player_points += abs(first_player_card - second_player_card)
    elif first_player_card < second_player_card:
        second_player_points += abs(first_player_card - second_player_card)
    else:
        print('Number wars!')
        first_player_card = int(command)
        second_player_card = int(input())
        if first_player_card < second_player_card:
            print(f'{name_of_first_player} is winner with {first_player_points} points')

        else:
            print(f'{name_of_second_player} is winner with {second_player_points} points')
        break
        
    command = input()
    if command == 'End of game':
        print(f'{name_of_first_player} has {first_player_points} points')
        print(f'{name_of_second_player} has {second_player_points} points')
