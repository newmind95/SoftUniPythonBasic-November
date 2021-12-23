number_of_days_of_tournament = int(input())

raised_money = 0
counter_win = 0
counter_lose = 0
result = ''

for tournament in range(number_of_days_of_tournament):
    command = input()
    daily_money = 0
    daily_win = 0
    daily_lose = 0
    
    while command != 'Finish':
        type_of_sport = input()

        if type_of_sport == 'win':
            daily_money += 20
            daily_win += 1
        elif type_of_sport == 'lose':
            daily_money += 0
            daily_lose += 1

        command = input()

    if daily_win > daily_lose:
        daily_money += daily_money * (10 / 100)
        counter_win += 1
    else:
        counter_lose += 1

    raised_money += daily_money
    
is_tournament_won = counter_win > counter_lose
    
if is_tournament_won:
    raised_money += raised_money * (20 / 100)
    result = f'You won the tournament! Total raised money: {raised_money:.2f}'
else:
    result = f'You lost the tournament! Total raised money: {raised_money:.2f}'
    
print(result)
