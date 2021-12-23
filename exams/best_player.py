flag = False
best_player_name = ''
best_player_score = 0

while True:

    player_name = input()
    if player_name == 'END':
        flag = True
        break

    number_of_goals = int(input())

    if number_of_goals > best_player_score:
        best_player_name = player_name
        best_player_score = number_of_goals

    if number_of_goals >= 10:
        flag = True
        break
    

print('%s is the best player!' % best_player_name)
if number_of_goals >= 3:
    print('He has scored %d goals and made a hat-trick !!!' % (best_player_score))
else:
    print('He has scored %d goals.' % best_player_score)

    
