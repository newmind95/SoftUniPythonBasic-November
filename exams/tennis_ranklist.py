number_of_tournaments = int(input())
starting_points_in_ranklist = int(input())
final_points = starting_points_in_ranklist
points = 0
counter_wins = 0

for tournaments in range(1, number_of_tournaments + 1):
    reached_stage_of_tournament = input()

    if reached_stage_of_tournament == 'W':
        points += 2000
        counter_wins += 1
    elif reached_stage_of_tournament == 'F':
        points += 1200
    elif reached_stage_of_tournament == 'SF':
        points += 720

average_points = int(points / number_of_tournaments)
percentage_won_tournaments = (counter_wins / number_of_tournaments) * 100
print(f'Final points: {final_points+points}')
print(f'Average points: {average_points}')
print(f'{percentage_won_tournaments:.2f}%')
