counter_win = 0
counter_lose = 0
total_matches = 0

while True:
    name_of_tournament = input()
    
    if name_of_tournament == 'End of tournaments':
        break

    number_of_games = int(input())
    total_matches += number_of_games

    for game in range(1, number_of_games + 1):
        
        home_points = int(input())
        away_points = int(input())
        home = abs(home_points - away_points)
        away = abs(home_points - away_points)

        if home_points > away_points:
            print(f'Game: {game} of tournament {name_of_tournament}: '
                  f'win with: {home} points.')
            counter_win += 1
            
        elif home_points < away_points:
            print(f'Game: {game} of tournament {name_of_tournament}: '
                  f'lost with: {away} points.')
            counter_lose += 1
        

percentage_of_wins = (counter_win / total_matches) * 100
percentage_of_losts = (counter_lose / total_matches) * 100
print(f'{percentage_of_wins:.2f}% matches win')
print(f'{percentage_of_losts:.2f}% matches lost')
        
