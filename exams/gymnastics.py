country = input()
instrument = input()

max_points = 20
hard_points = 0
performance = 0

if instrument == 'ribbon':
    if country == 'Russia':
        hard_points = 9.100
        performance = 9.400
    elif country == 'Bulgaria':
        hard_points = 9.600
        performance = 9.400
    elif country == 'Italy':
        hard_points = 9.200
        performance = 9.500

elif instrument == 'hoop':
    if country == 'Russia':
        hard_points = 9.300
        performance = 9.800
    elif country == 'Bulgaria':
        hard_points = 9.550
        performance = 9.750
    elif country == 'Italy':
        hard_points = 9.450
        performance = 9.350

elif instrument == 'rope':
    if country == 'Russia':
        hard_points = 9.600
        performance = 9.000
    elif country == 'Bulgaria':
        hard_points = 9.500
        performance = 9.400
    elif country == 'Italy':
        hard_points = 9.700
        performance = 9.150

total_points = hard_points + performance
difference = abs(max_points - total_points)
percentage_of_lack = (difference / max_points) * 100
print(f'The team of {country} get {total_points:.3f} on {instrument}.')
print(f'{percentage_of_lack:.2f}%')
