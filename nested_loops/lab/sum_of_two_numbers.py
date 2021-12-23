start = int(input())
final = int(input())
magic_number = int(input())

is_combination_found = False
counter_combinations = 0

for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        counter_combinations += 1
        if first_number + second_number == magic_number:
            is_combination_found = True
            break

    if is_combination_found:
        break


if is_combination_found:
    print(f'Combination N:{counter_combinations}'
          f' ({first_number} + {second_number} = {magic_number})')
else:
    print(f'{counter_combinations} - neither equals {magic_number}')
