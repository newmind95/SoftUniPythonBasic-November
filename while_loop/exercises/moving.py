width = int(input())
length = int(input())
height = int(input())

total_cubic_meters_availability = width * length * height
cubic_meters = 0
difference = 0
free_cubic_meters = 0
is_meters_left = True
command = input()

while command != 'Done':
    number_of_packages = int(command)
    cubic_meters += number_of_packages
    free_cubic_meters += number_of_packages

    if total_cubic_meters_availability < cubic_meters:
        is_meters_left = False
        break
    
    command = input()

difference = abs(total_cubic_meters_availability - cubic_meters)
if is_meters_left:
    print("%d Cubic meters left." % free_cubic_meters)
else:
    print("No more free space! You need %d Cubic meters more." % difference)
