number_of_floors = int(input())
number_of_rooms = int(input())
result = ''

for floor in range(number_of_floors, 0, -1):
    for room in range(number_of_rooms):
        if floor >= number_of_floors:
            result = 'L'
        elif floor % 2 == 0:
            result = 'O'
        else:
            result = 'A'

        print(f'{result}{floor}{room}', end=' ')
    print()
