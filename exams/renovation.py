from math import ceil

height = int(input())
width = int(input())
percentage_not_be_painted = int(input())
walls = height * width * 4
walls = ceil(walls - (walls * (percentage_not_be_painted / 100)))

command = input()

while command != 'Tired!':
    liters_paint = int(command)

    walls -= liters_paint

    if walls <= 0:
        break
    
    command = input()

if walls > 0:
    print(f'{walls} quadratic m left.')
elif walls == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(walls)} l paint left!")
