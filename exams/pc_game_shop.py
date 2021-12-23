number_of_sold_games = int(input())
counter_of_hearthstone = 0
counter_of_fornite = 0
counter_of_overwatch = 0
counter_others = 0

for games in range(1, number_of_sold_games + 1):

    name_of_game = input()

    if name_of_game == 'Hearthstone':
        counter_of_hearthstone += 1
    elif name_of_game == 'Fornite':
        counter_of_fornite += 1
    elif name_of_game == 'Overwatch':
        counter_of_overwatch += 1
    else:
        counter_others += 1

percentage_hearthstone_sold = (counter_of_hearthstone / number_of_sold_games) * 100
percentage_fornite_sold = (counter_of_fornite / number_of_sold_games) * 100
percentage_overwatch_sold = (counter_of_overwatch / number_of_sold_games) * 100
percentage_others_sold = (counter_others / number_of_sold_games) * 100

print(f'Hearthstone - {percentage_hearthstone_sold:.2f}%')
print(f'Fornite - {percentage_fornite_sold:.2f}%')
print(f'Overwatch - {percentage_overwatch_sold:.2f}%')
print(f'Others - {percentage_others_sold:.2f}%')
