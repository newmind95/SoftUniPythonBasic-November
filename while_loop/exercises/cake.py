length = int(input())
width = int(input())
is_cake_end = False
total_pieces = width * length
sum_of_pieces = 0

while total_pieces >= 0:
    command = input()

    if command == 'STOP':
        is_cake_end = True
        break
    else:
        sum_of_pieces = int(command)
        total_pieces = total_pieces - sum_of_pieces

if sum_of_pieces > total_pieces:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
else:
    print(f'{total_pieces} pieces are left.')

