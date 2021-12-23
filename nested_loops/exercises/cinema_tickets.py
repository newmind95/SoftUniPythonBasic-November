movie_name = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
counter_tickets = 0
total_tickets_counter = 0

while movie_name != 'Finish':
    free_seats = int(input())
    count_free_spaces = free_seats
    sold_tickets = 0
    while free_seats > 0:
        type_of_ticket = input()
        if type_of_ticket == 'End':
            break
        
        if type_of_ticket == 'student':
            student_tickets += 1
        elif type_of_ticket == 'standard':
            standard_tickets += 1
        elif type_of_ticket == 'kid':
            kid_tickets += 1
        
        free_seats = free_seats -1
        sold_tickets += 1
        total_tickets_counter += 1
        
    print(f'{movie_name} - {sold_tickets / count_free_spaces * 100:.2f}% full.')
    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets_counter * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets_counter * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets_counter * 100:.2f}% kids tickets.')
