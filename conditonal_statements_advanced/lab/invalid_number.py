number = int(input())

is_valid_number = 100 <= number <= 200 or number == 0

if is_valid_number:
    print()
elif not is_valid_number:
    print('invalid')