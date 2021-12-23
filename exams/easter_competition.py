number_of_easter_bread = int(input())
best_points = 0
best_name_of_baker = 0

for baker in range(number_of_easter_bread):
    name_of_baker = input()
    command = input()
    points = 0

    while command != 'Stop':
        grade = int(command)

        points += grade
        command = input()

    if command == 'Stop':
        print(f'{name_of_baker} has {points} points.')

    if points > best_points:
        best_points = points
        best_name_of_baker = name_of_baker
        print(f'{best_name_of_baker} is the new number 1!')

print(f'{best_name_of_baker} won competition with {best_points} points!')
