number_of_days = int(input())
number_of_hours = int(input())
tax = 0
total_tax = 0

for day in range(1, number_of_days + 1):
    day_tax = 0
    for hour in range(1, number_of_hours + 1):
        
        if day % 2 == 0 and hour % 2 != 0:
            tax = 2.50
            day_tax += tax
        elif day % 2 != 0 and hour % 2 == 0:
            tax = 1.25
            day_tax += tax
        else:
            tax = 1
            day_tax += tax

    total_tax += day_tax

    print(f'Day: {day} - {day_tax:.2f}')

print(f'Tax = {total_tax:.2f}')
    
